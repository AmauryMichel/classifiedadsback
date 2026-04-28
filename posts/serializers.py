from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    creator_data = UserSerializer(read_only=True, source='creator')

    class Meta:
        model = Post
        fields = ["url", "id", "creator", "creator_data", "title", "text", "active", "creation_date", "categories"]