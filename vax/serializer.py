from rest_framework import serializers
from .models import MyUser, Center
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'
