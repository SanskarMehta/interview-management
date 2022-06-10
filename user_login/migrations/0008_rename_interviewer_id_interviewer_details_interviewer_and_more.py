# Generated by Django 4.0.5 on 2022-06-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0007_interviewer_details_interviewer_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewer_details',
            old_name='interviewer_id',
            new_name='interviewer',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='user_10th_marks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='user_12th_marks',
            field=models.FloatField(),
        ),
    ]
