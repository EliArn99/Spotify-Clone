from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'music/index.html')

def login(request):
    return render(request, 'music/login.html')

def signup(request):
    return render(request, 'music/signup.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def music(request):
    return render(request, 'music/music.html')

def profile(request):
    return render(request, 'music/profile.html')

def search(request):
    return render(request, 'music/search.html')
