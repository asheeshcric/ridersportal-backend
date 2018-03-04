from django.contrib.auth.models import User
from ..models import UserDetails

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'username')


class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserDetails
        fields = ('user', 'address', 'contact', 'bike_model')