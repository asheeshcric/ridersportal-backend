from django.contrib.auth.models import User
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('email', 'password', 'token')