from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_id = models.CharField(max_length=255, null=True)
    task_title = models.CharField(max_length=255, null=True)
    task_discription = models.CharField(max_length=255, null=True)
    original_estimate = models.IntegerField(null=True)
    duration = models.CharField(max_length=255, null=True)
    task_status = models.CharField(max_length=255, null=True)
    assigned_user = models.CharField(max_length=255, null=True)
    project_name = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
