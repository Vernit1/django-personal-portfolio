# Generated by Django 3.0.8 on 2020-07-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0002_auto_20200715_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deleteTodoOrNot',
            field=models.BooleanField(default=False),
        ),
    ]