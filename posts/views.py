from django.shortcuts import render
from rest_framework import permissions, viewsets

from posts.models import Post, Category
from posts.serializers import PostSerializer, CategorySerializer


class PostPermission(permissions.BasePermission):      
    def has_permission(self, request, view):
        if request.user.is_superuser:            
            return True

        if view.action == 'create':
            # Check if user ID matches the request's creator's ID 
            return 'creator' in request.data and request.data['creator'] == request.user.id
        
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_superuser
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]



class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        
        return request.user.is_superuser

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission]