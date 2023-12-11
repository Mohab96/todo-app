from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('tags', views.TagViewSet, basename='tags')
router.register('taggedTasks', views.TaggedTaskViewSet,
                basename='tagged-tasks')
router.register('users', views.UserViewSet)
router.register('reminders', views.ReminderViewSet, basename='reminders')

urlpatterns = [
    path('search/', views.search),
    path('play/', views.playground),
] + router.urls
