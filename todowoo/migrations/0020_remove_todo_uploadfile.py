# Generated by Django 3.0.8 on 2020-08-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0019_auto_20200802_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='uploadFile',
        ),
    ]