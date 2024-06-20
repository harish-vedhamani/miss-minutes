import imp
from django.conf import settings as conf_settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from rest_framework import status
from fnps_be.utils import Error

# decorator method for check user is authorised
def user_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        secret_key = conf_settings.SECRET_KEY
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return Error("Unauthorized!", status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload =  jwt.decode(token, secret_key, algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            return Error("Unauthorized!", status=status.HTTP_401_UNAUTHORIZED)

        if payload['scope'] == 'user':
            current_user = User.objects.filter(access_token=token).first()
        else:
            return Error("Unauthorized!", status=status.HTTP_401_UNAUTHORIZED)

        if current_user is None or current_user.id != payload['id']:
            return Error("Unauthorized!", status=status.HTTP_401_UNAUTHORIZED)

        return view_func(request, current_user, *args, **kwargs)

    return wrapper
