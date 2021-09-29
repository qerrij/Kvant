from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about-us.html')


def user_logout(request):
    logout(request)
    return redirect('home')