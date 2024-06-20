from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [ 'id', 'name', 'email', 'access_token', 'password',  'is_admin', 'created_at' ]
        
        extra_kwargs = {
            'access_token': { 'write_only': True },
            'password': { 'write_only': True },
        }   

        # def create(self, validated_data):
        #     password = validated_data.pop('password', None)

        #     if password is not None:
        #         validated_data['password'] = make_password(password)
                
        #     # for demo purpose need to remove after develop
        #     if password is None:
        #         validated_data['password'] = make_password("Password@123")

        #     instance = self.Meta.model(**validated_data)
        #     instance.save()

        #     return instance