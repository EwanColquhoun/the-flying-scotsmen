from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    """
    Modifies the default DjangoUser model to include the below.
    """
    message = models.TextField(blank=False, null=False, help_text='Required')
    email = models.CharField(max_length=100, blank=False, null=False)
    objects = UserManager()

    def __str__(self):
        return str(self.username)


class GroupMember(models.Model):
    """
    The class for The Flying Scotsmen group members to allow access to booking and calender functions.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                unique=True,
                                null=True,
                                related_name='registered')
    registered = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)
