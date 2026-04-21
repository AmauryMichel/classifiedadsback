from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from posts.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["url", "id", "creator", "title", "text", "active", "creation_date", "categories"]