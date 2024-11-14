from django.urls import path
from .views import TaskListCreateView, TaskDetailView
from django.contrib.auth import get_user_model

User = get_user_model()

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task_list_create'),
    path('<int:pk/>', TaskDetailView.as_view(), name='task_detail'),
]
