# Generated by Django 5.1 on 2025-02-19 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerprofile',
            name='user',
        ),
    ]
