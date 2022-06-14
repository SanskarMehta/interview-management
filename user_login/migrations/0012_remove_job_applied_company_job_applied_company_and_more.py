# Generated by Django 4.0.5 on 2022-06-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0011_job_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_applied',
            name='company',
        ),
        migrations.AddField(
            model_name='job_applied',
            name='company',
            field=models.ManyToManyField(default='None', to='user_login.company_details'),
        ),
        migrations.RemoveField(
            model_name='job_applied',
            name='user',
        ),
        migrations.AddField(
            model_name='job_applied',
            name='user',
            field=models.ManyToManyField(default='None', to='user_login.user_details'),
        ),
    ]