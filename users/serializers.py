from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = []

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ["url", "id", "email", "password", "first_name", "last_name"]