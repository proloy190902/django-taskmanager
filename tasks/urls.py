# tasks/urls.py
from django.urls import path

from .views import ListTask, DetailTask
from tasks.views import index,details
urlpatterns = [
    path('', ListTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
  
    
]