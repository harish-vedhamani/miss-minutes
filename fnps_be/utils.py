import uuid 
import random
import datetime
from django.conf import settings as conf_settings
from rest_framework.response import Response
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def Error(errors, status):
    if isinstance(errors, list):
        return Response({ 'errors': errors }, status)
    else:
        return Response({ 'errors': [ errors ] }, status)
    
def Format(errors):
    array = []
    for key, value in errors.items():
        temp = key + " - " + ', '.join(value)
        array.append(temp)
    return array
