import django.contrib.auth.models
from django.db import models
from django import forms
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')


# class Friend(User, models.Model):
#     user = models.ForeignKey(
#         'User',
#         on_delete=models.CASCADE)
#     friend = models.ForeignKey(
#         'User',
#         on_delete=models.CASCADE)

