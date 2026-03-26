from django.shortcuts import render
from rest_framework import permissions, viewsets

from users.models import User
from users.serializers import UserSerializer

# API endpoint that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []