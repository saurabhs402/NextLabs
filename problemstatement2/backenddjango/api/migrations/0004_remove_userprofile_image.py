# Generated by Django 5.0.4 on 2024-04-30 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_admin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
