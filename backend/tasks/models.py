from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ('Open','Open'),
        ('In Progress','InProgress'),
        ('Completed','Completed'),
    ]
    title = models.CharField(max_length=255)
    decription = models.TextField()
    assigned_to = models.ForeignKey(User, related_name='assigned_task', on_delete=models.SET_NULL,null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_task', on_delete=models.CASCADE)
    status =models.CharField(max_length=20,choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
# Create your models here.
