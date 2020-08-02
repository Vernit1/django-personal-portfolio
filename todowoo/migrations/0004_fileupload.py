# Generated by Django 3.0.8 on 2020-07-29 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import todowoo.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todowoo', '0003_auto_20200715_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadFile', models.FileField(upload_to=todowoo.models.get_upload_path)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
