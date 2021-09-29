from django.db import models
from django import forms

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')

