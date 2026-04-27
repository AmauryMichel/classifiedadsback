from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    permission_classes = []

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ["url", "id", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)