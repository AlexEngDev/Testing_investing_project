from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from main.models import New


def index(request):
    return render(request, 'main/home.html')


def news(request):
    new = New.objects.order_by('-date')[:10]
    return render(request, 'main/news.html', {'new': new})


def analysis(request):
    return render(request, 'main/analysis.html')


def services(request):
    return render(request, 'main/services.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'formAuth': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html',
                          {'formAuth': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('main:signupuser')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'main/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main:index')
            except IntegrityError:
                return render(request, 'main/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'That username has already been taken. '
                                                                         'Please choose a new username'})
        else:
            return render(request, 'main/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})
