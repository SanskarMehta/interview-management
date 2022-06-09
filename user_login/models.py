from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField


class CustomUser(AbstractUser):
    Is_interviewer = models.BooleanField(default=False)
    Is_first_time = models.BooleanField(default=True)


class user_details(models.Model):
    user_phone = PhoneNumberField()
    user_technology = models.CharField(max_length=30)
    user_12th_marks = models.IntegerField()
    user_10th_marks = models.IntegerField()
    user_CPI = models.FloatField()
    user_CV = models.FileField()
    accepted_status = models.BooleanField(default=False)