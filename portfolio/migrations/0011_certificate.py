# Generated by Django 3.0.8 on 2020-08-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('issuedby', models.CharField(max_length=50)),
                ('issuedDate', models.DateField()),
                ('url', models.URLField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='certificates/')),
            ],
        ),
    ]
