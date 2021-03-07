# Generated by Django 3.1 on 2021-03-06 04:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded', models.DateTimeField()),
                ('host', models.CharField(max_length=100)),
                ('participants', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=' ', max_length=100), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded', models.DateTimeField()),
            ],
        ),
    ]
