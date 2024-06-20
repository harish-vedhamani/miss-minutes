from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(default=timezone.now)

