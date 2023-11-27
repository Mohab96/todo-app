from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)
router.register('taggedTasks', views.TaggedTaskViewSet)

urlpatterns = [
    path('hello/', views.hello)
] + router.urls
