from django.db import models

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000, blank=True)
    active = models.BooleanField(default=False)
    creation_date = models.DateField(null=True)
    categories = models.ManyToManyField(Category, blank=True)