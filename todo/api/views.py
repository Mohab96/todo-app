from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import *


@api_view(['GET'])
def hello(request):
    return Response('ok')


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return EditTaskSerializer
        else:
            return TaskSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TaggedTaskViewSet(ModelViewSet):
    serializer_class = TaggedTaskSerializer
    queryset = TaggedTask.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return EditTaggedTaskSerializer
        else:
            return TaggedTaskSerializer
