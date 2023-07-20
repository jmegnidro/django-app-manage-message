
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=125)
    first_name = models.CharField(max_length=125)
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to='photo')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'username']
    UNIQUE_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
