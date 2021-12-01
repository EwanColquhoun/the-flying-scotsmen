from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    message = models.TextField(blank=False, null=False, help_text='Required, Why do you want to join The Flying Scotsmen?')