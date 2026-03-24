from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    is_staff = None
    last_login = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []