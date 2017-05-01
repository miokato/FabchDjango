# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0015_lecture_pub_date'),
        ('accounts', '0002_auto_20161127_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('watch_history', models.ManyToManyField(to='classes.Lecture')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='watch_history',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
