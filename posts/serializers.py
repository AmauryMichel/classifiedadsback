from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.serializers import UserSerializer
from posts.models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "id", "name", "description"]

class PostSerializer(serializers.ModelSerializer):
    creator_data = UserSerializer(read_only=True, source='creator')
    categories_info = CategorySerializer(read_only=True, source='categories', many=True)

    class Meta:
        model = Post
        fields = ["url", "id", "creator", "creator_data", "title", "text", "active", "creation_date", "categories", "categories_info"]
        extra_kwargs = {
            'creator': {'write_only': True},
        }