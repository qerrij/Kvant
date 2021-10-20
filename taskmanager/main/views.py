from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from .forms import CreationProject
from .models import *


def index(request):
    # if request.method == 'POST':
    #     form = AddFriend(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = AddFriend()
    #     if request.user.is_authenticated == True:
    #         form.initial['user'] = request.username
    return render(request, 'main/index.html')


def personal_area(request):
    if request.method == 'POST':
        form = CreationProject(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = CreationProject()
    return render(request,  'main/about-us.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)