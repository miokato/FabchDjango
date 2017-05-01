# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_auto_20161122_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(max_length=50)),
                ('lecture_desc', models.CharField(max_length=200)),
                ('video_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Classes',
            new_name='Klass',
        ),
        migrations.DeleteModel(
            name='Lectures',
        ),
        migrations.RenameField(
            model_name='klass',
            old_name='class_desc',
            new_name='klass_desc',
        ),
        migrations.RenameField(
            model_name='klass',
            old_name='class_id',
            new_name='klass_id',
        ),
        migrations.RenameField(
            model_name='klass',
            old_name='class_name',
            new_name='klass_name',
        ),
        migrations.AddField(
            model_name='lecture',
            name='klass_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Klass'),
        ),
    ]