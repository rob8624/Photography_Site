# Generated by Django 4.1 on 2022-11-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_settings_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='profile_bio',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
