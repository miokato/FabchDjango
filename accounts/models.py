from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import User
from classes.models import Lecture


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    watch_history = models.ManyToManyField(Lecture)



