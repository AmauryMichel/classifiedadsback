from django.shortcuts import render
from rest_framework import permissions, viewsets

from users.models import User
from users.serializers import UserSerializer

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if view.action == 'create':
            return True
        elif view.action in ['list', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        
        return False

# API endpoint that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]