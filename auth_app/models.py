from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    u_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email