from rest_framework import serializers
from .models import *
from auth.models import User
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        name = attrs['name']
        user = self.context['request'].user

        if Category.objects.filter(name=name, user=user).exists():
            raise serializers.ValidationError(
                'This category already exists')

        # super.validate(attrs)
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        name = validated_data['name']

        category = Category.objects.create(user=user, name=name)

        return category

    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
        read_only_fields = ('user', 'id')


class TagSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        name = attrs['name']
        user = self.context['request'].user

        if Tag.objects.filter(name=name, user=user).exists():
            raise serializers.ValidationError(
                'This tag already exists')

        # super.validate(attrs)
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        name = validated_data['name']

        tag = Tag.objects.create(user=user, name=name)

        return tag

    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']
        read_only_fields = ('user', 'id')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'body', 'repeat', 'priority',
                  'notes', 'status', 'category', 'user']
        read_only_fields = ('user', 'id')


class CreateTaskSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        body = self.data['body']
        user = self.context['request'].user

        task = Task.objects.create(body=body, user=user)
        task.save()

        return task

    class Meta:
        model = Task
        fields = ['id', 'user', 'body']
        read_only_fields = ('user', 'id')


class EditTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'body', 'repeat', 'priority',
                  'notes', 'status', 'category']

        read_only_fields = ('user', 'id')


class TaggedTaskSerializer(serializers.ModelSerializer):
    def validate_task(self, value):
        user = self.context['request'].user
        if not Task.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                'This task does not belong to this user')
        return value

    class Meta:
        model = TaggedTask
        fields = ['id', 'task', 'tag']


class EditTaggedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedTask
        fields = ['id', 'task', 'tag']


class UserSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'is_staff', 'is_active']

        read_only_fields = ('id',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'task', 'date']


class ReminderCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        task = attrs['task']
        user = self.context['request'].user

        if not Task.objects.filter(id=task.id, user=user).exists():
            raise serializers.ValidationError(
                'This task does not belong to that user')

        # super.validate(attrs)
        return attrs

    class Meta:
        model = Reminder
        fields = ['id', 'task', 'date']


class ReminderUpdateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        task_date = attrs['date'].__str__()
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if task_date < current_date:
            raise serializers.ValidationError('Choose a date in the future')

        # super.validate(attrs)
        return attrs

    class Meta:
        model = Reminder
        fields = ['id', 'task', 'date']
        read_only_fields = ('id', 'task')
