# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 13:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20160701_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfiles',
            name='time_of_uploading',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]