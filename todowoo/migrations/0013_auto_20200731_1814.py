# Generated by Django 3.0.8 on 2020-07-31 12:44

from django.db import migrations, models
import todowoo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0012_auto_20200731_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='uploadFile',
            field=models.FileField(null=True, upload_to=todowoo.models.get_upload_path),
        ),
    ]