from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User
from users.serializers import UserSerializer
from posts.serializers import PostSerializer

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if view.action == 'create':
            return True
        elif view.action in ['list', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        
        return False
        
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser

# API endpoint that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    
    @action(detail=True, methods=['get'], serializer_class=PostSerializer)
    def posts(self, request, pk):
        listPosts = self.get_object().posts.all()
        serializer = self.get_serializer(instance=listPosts, many = True)
        
        return Response(serializer.data)