# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250)),
                ('time_of_uploading', models.CharField(max_length=250)),
                ('type_of_file', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]
