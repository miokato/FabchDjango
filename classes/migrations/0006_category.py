# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20161122_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_desc', models.CharField(max_length=200)),
                ('test', models.CharField(max_length=200)),
            ],
        ),
    ]
