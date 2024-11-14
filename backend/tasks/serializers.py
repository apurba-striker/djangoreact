from rest_framework import serializers
from models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.username')
    assigned_to = serializers.SlugRelatedField(slug_field='username',queryset = User.objects.all(),required=False,allow_null = True)
    
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_by', 'status', 'created_at','updated_at']