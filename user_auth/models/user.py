from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    reputation = models.FloatField(default=0)

