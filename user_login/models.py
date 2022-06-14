from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

application_choices = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
)


class CustomUser(AbstractUser):
    Is_interviewer = models.BooleanField(default=False)
    Is_first_time = models.BooleanField(default=True)


class user_details(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=12)
    user_technology = models.CharField(max_length=30)
    user_12th_marks = models.FloatField()
    user_10th_marks = models.FloatField()
    user_CPI = models.FloatField()
    user_CV = models.FileField(upload_to='CV/', validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
    accepted_status = models.BooleanField(default=False)


class interviewer_details(models.Model):
    interviewer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    interviewer_phone = models.CharField(max_length=12)
    interviewer_technology = models.CharField(max_length=30)
    interviewer_job_role = models.CharField(max_length=30)
    interviewer_experience = models.CharField(max_length=20)


class company_details(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100, default='Software Engineer')
    job_location = models.CharField(max_length=100, default='remote')
    job_description = models.CharField(max_length=300, default="None")


class job_applied(models.Model):
    user = models.ForeignKey(user_details, on_delete=models.CASCADE, default=5)
    company = models.ForeignKey(company_details, on_delete=models.CASCADE, default=1)
    application_status = models.CharField(max_length=40, choices=application_choices, default='Pending')

