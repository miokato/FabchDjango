from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    klass_name = models.CharField(max_length=100, null=True)
    klass_desc = models.CharField(max_length=200, null=True)
    klass_img = models.URLField(max_length=300, null=True)
    lecture_num = models.IntegerField(default=0)
    lecture_name = models.CharField(max_length=50, null=True)
    lecture_desc = models.CharField(max_length=200, null=True)
    video_number = models.IntegerField(default=0)
    category = models.ForeignKey('Category', default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.klass_name
