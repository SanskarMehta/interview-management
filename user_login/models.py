from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Is_interviewer = models.BooleanField(default=False)

