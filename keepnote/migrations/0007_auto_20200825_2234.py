# Generated by Django 3.0.8 on 2020-08-25 17:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keepnote', '0006_imageuploadinnotes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageUploadInNotes',
            new_name='ImageUploadInNote',
        ),
    ]
