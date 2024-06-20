from django.shortcuts import render
from .models import Task  

# Create your views here.
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.decorators import api_view
from fnps_be.decorators import user_login_required
from task.serializers import TaskSerializer
from fnps_be.utils import Error, Format

import jwt, datetime
from django.utils import timezone
# from django.conf import settings as conf_settings

# Documentation 

@api_view(['POST', 'GET'])
@user_login_required
def task_view(request, current_user, *args, **kwargs):
    if request.method == 'POST':
        data = request.data.copy()
        
        # Handle multiple tasks
        if isinstance(data, list):
            for task_data in data:
                task_data['assigned_user'] = current_user.name
            serializer = TaskSerializer(data=data, many=True)
        else:
            data['assigned_user'] = current_user.name
            serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response({'task': serializer.data})