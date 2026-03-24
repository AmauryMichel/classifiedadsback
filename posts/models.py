from django.db import models

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField
    status = models.BooleanField(default=False)
    creation_date = models.DateField
    categories = models.ManyToManyField(Category)