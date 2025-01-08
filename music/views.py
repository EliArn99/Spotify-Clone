from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'music/index.html')

def login(request):
    return render(request, 'music/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
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
