
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasksListAPI, name='tasksListAPI'),
    path('taskDetailAPI/<int:task_id>', views.taskDetailAPI, name='taskDetailAPI'),
]