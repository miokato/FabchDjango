# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 17:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_auto_20161125_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
