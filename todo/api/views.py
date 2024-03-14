from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.conf import settings
from django.core.mail import send_mail
import asyncio


@api_view(['GET'])
@permission_classes([AllowAny])
def playground(request):
    pass


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search(request):
    # search in the tasks for the currently authenticated(logged in) user
    current_user_id = request.user.id
    query = request.data['query']

    searchResult = Task.objects.filter(
        user__id=current_user_id, body__icontains=query)
    serializer = TaskSerializer(searchResult, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTaskSerializer
        elif self.request.method == 'PUT':
            return EditTaskSerializer
        else:
            return TaskSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()

        return Task.objects.filter(user=user)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Category.objects.all()

        return Category.objects.filter(user=user)


class TagViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Tag.objects.all()

        return Tag.objects.filter(user=user)


class TaggedTaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaggedTaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return EditTaggedTaskSerializer
        else:
            return TaggedTaskSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return TaggedTask.objects.all()

        return TaggedTask.objects.filter(task__user=user)


class UserViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class ReminderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ReminderUpdateSerializer
        elif self.request.method == 'POST':
            return ReminderCreateSerializer
        return ReminderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Reminder.objects.all()

        return Reminder.objects.filter(task__user=user)
