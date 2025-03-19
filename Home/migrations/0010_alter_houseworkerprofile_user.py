# Generated by Django 5.1 on 2025-02-20 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_houseworkerprofile_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseworkerprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houseworker_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
