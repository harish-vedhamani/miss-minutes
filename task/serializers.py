from rest_framework import serializers
from .models import Task
from django.contrib.auth.hashers import make_password

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = [ 'id', 'task_id', 'task_title', 'task_discription', 'original_estimate',  'duration', 'task_status', 'assigned_user', 'project_name', 'date' ]