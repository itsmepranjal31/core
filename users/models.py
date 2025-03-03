
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    codeforces_username = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username
