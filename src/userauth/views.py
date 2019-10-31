from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms


def home(request):
    return render(request, 'home.html', {})


def user_profile(request):
    return render(request, 'profile.html', {})


def user_login(request):
    form = forms.LoginUser(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('you have successfully logged in!'))
            return redirect('profile')
        else:
            messages.success(request, ('Incorrect username or password...Please try again!'))
            return redirect('login')

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, ('You have been successfully logged out!'))
    return render(request, 'home.html', {})


def user_register(request):
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        user.save()
        # login_user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, ('You have successfully registered and logged in!'))
        return redirect('profile')
    else:
        return render(request, 'register.html', {'form': form})
