# Generated by Django 3.0.8 on 2020-08-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keepnote', '0003_auto_20200825_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
