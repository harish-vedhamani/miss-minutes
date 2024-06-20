from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings as conf_settings
from fnps_be.decorators import user_login_required
from fnps_be.utils import Error
from django.contrib.auth.hashers import check_password

from .serializers import UserSerializer
from .models import User
import jwt, datetime
from django.utils import timezone
# from django.conf import settings as conf_settings

# Documentation 

@api_view(['POST'])
def user_login_view(request):

    secret_key = conf_settings.SECRET_KEY
    expiry_time = conf_settings.ADMIN_SESSION_EXPIRY_TIME
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Error("Email or Password is can not be blank.", status=status.HTTP_406_NOT_ACCEPTABLE)

    user = User.objects.filter(email=email).first()

    if user is None:
        return Error("Email or Password is not correct.", status=status.HTTP_406_NOT_ACCEPTABLE)

    # if not user.check_password(password):
    #     return Error("Email or Password is not correct.", status=status.HTTP_406_NOT_ACCEPTABLE)

    payload = {
        'id': user.id,
        'name': user.name,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=expiry_time),
        'iat': datetime.datetime.utcnow(),
        'scope': 'user'
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')

    data_to_change = { 'access_token': token }

    serializer = UserSerializer(user, data=data_to_change, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        {   
            'id': user.id,
            'access_token': user.access_token,
            'email': user.email,
            'name': user.name,
        }
    )

@api_view(['DELETE'])
@user_login_required
def user_logout_view(request, current_user, *args, **kwargs):
    data_to_change = { 'access_token': None }

    serializer = UserSerializer(current_user, data=data_to_change, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(status= status.HTTP_204_NO_CONTENT)


