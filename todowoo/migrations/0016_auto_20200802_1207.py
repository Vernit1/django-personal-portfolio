# Generated by Django 3.0.8 on 2020-08-02 06:37

from django.db import migrations, models
import todowoo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0015_auto_20200802_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='uploadFile',
            field=models.FileField(blank=True, null=True, storage=todowoo.models.MyStorage(), upload_to=todowoo.models.get_upload_path),
        ),
    ]