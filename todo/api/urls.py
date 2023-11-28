from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)
router.register('taggedTasks', views.TaggedTaskViewSet)
router.register("users", views.UserViewSet)

urlpatterns = [
    path('export/', views.export),
    path('search/', views.search)
] + router.urls
