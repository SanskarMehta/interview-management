# Generated by Django 4.0.5 on 2022-06-14 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0010_company_details_alter_user_details_user_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_status', models.BooleanField(default='None', null=True)),
                ('company', models.OneToOneField(default='None', on_delete=django.db.models.deletion.CASCADE, to='user_login.company_details')),
                ('user', models.OneToOneField(default='None', on_delete=django.db.models.deletion.CASCADE, to='user_login.user_details')),
            ],
        ),
    ]