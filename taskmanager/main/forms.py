from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class CreationProject(ModelForm):
    name = forms.CharField(label='Название проекта', widget=forms.TextInput(attrs={'class': 'name'}))
    description = forms.CharField(label='Описание проекта', widget=forms.TextInput(attrs={'class': 'descr'}))
    file = forms.FileField()
    class Meta:
        model = Project
        fields = ['name', 'description', 'file']