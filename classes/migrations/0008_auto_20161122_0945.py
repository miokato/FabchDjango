# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_category_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='string',
        ),
        migrations.RemoveField(
            model_name='category',
            name='test',
        ),
    ]
