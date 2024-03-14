import asyncio
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from notificationapi_python_server_sdk import notificationapi


def validate_registration_data(data):
    username = data.get('username', None)
    email = data.get('email', None)
    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    password = data.get('password', None)
    confirm_password = data.get('confirm_password', None)

    errors = {}

    if not username:
        errors['username'] = 'Please enter your username'
    if not email:
        errors['email'] = 'Please enter your email'
    if not first_name:
        errors['first_name'] = 'Please enter your first name'
    if not last_name:
        errors['last_name'] = 'Please enter your last name'
    if not password:
        errors['password'] = 'Please enter password'
    if not confirm_password:
        errors['confirm_password'] = 'Please confirm your password'

    if password and confirm_password and password != confirm_password:
        errors['password'] = "Passwords don't match."

    try:
        validate_email(email)
    except ValidationError:
        if email:
            errors['email'] = "Enter a valid Email."

    if email and User.objects.filter(email=email).exists():
        errors['email'] = "Choose another email, this one already exists."

    return (True if len(errors) == 0 else False, errors)


@api_view(['POST'])
def register(request):
    username = request.data.get('username', None)
    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)

    valid, errors = validate_registration_data(request.data)

    if not valid:
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )

    refresh = RefreshToken.for_user(user)

    return Response({
        'message': 'User successfully registered.',
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_password(request):
    current_password = request.data.get('current_password', False)
    new_password = request.data.get('new_password', False)

    if not current_password or not new_password:
        return Response({
            'error': 'Please enter your current password and new password'
        }, status=status.HTTP_400_BAD_REQUEST)

    if request.user.check_password(current_password):
        request.user.set_password(new_password)
        request.user.save()

        return Response({
            'message': 'Password updated successfully'
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Wrong Password'
        }, status=status.HTTP_400_BAD_REQUEST)


def SendEmail():
    pass


@api_view(['POST'])
def forgot_password(request):
    email = request.data['email']
    current_url = request.build_absolute_uri() \
        .replace('/forgot_password/', '/reset_password/')

    try:
        user = User.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        token = default_token_generator.make_token(user)
        reset_url = f"{current_url}{uid}/{token}"
        SendEmail(reset_url, user)

    except User.DoesNotExist:
        return Response({"There isn't any user found with this email"},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "success": "Instructions were sent to your mail successfully!"
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.set_password(request.data['password'])
        user.save()
        return Response({'success': 'Password has been reset.'},
                        status=status.HTTP_200_OK)
    return Response({'error': 'Invalid reset URL.'},
                    status=status.HTTP_400_BAD_REQUEST)
