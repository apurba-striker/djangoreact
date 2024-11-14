from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.exceptions import PermissionDenied
User = get_user_model()

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class= TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_update(self, serializer):
        task  = self.get_object()
        if task.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this task")
        serializer.save()
    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.delete()
    
# Create your views here.
