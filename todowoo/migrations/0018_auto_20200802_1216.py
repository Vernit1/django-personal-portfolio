# Generated by Django 3.0.8 on 2020-08-02 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todowoo', '0017_auto_20200802_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='user',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
