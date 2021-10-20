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


# class AddFriend(ModelForm):
#     # user = forms.ChoiceField(widget=forms.Select, choices=User)
#     # friend = forms.ChoiceField(widget=forms.Select, choices=User)
#     #
#     # class Meta:
#     #     model = Friend
#     #     fields = ['user', 'friend']
#     class Meta:
#         users = [i.username for i in User.objects.raw('SELECT id FROM main_customuser')]
#         # print(users)
#         model = Friend
#         fields = ['user', 'friend']
#         widgets = {
#             'user': forms.HiddenInput(),
#             'friend': forms.Select(choices=users)
#         }