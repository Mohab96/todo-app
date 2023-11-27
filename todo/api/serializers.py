from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'body', 'repeat', 'priority',
                  'notes', 'status', 'category', 'user']


class EditTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'body', 'repeat', 'priority',
                  'notes', 'status', 'category', 'user']

        read_only_fields = ('user',)


class TaggedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedTask
        fields = ['id', 'task', 'tag']


class EditTaggedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedTask
        fields = ['id', 'task', 'tag']
        read_only_fields = ('task',)
