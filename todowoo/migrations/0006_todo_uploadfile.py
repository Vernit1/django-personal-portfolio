# Generated by Django 3.0.8 on 2020-07-31 07:55

from django.db import migrations, models
import todowoo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0005_fileupload_todoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='uploadFile',
            field=models.FileField(null=True, upload_to=todowoo.models.get_upload_path),
        ),
    ]