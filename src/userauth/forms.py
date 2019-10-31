from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


class LoginUser(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Username'}))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Username'}))

    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'First name'}))

    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Last name'}))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Enter email'}))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control', 'placeholder': 'Confirm password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username)
        if user_exists.exists():
            raise forms.ValidationError('Username is taken...Try another!')
        elif username.isdigit():
            raise forms.ValidationError('Username must contain both letters and numbers!')
        elif username.isalpha():
            raise forms.ValidationError('Username must contain both letters and numbers!')
        else:
            return username

    def clean_first_name(self):
        # data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        # full_name = User.objects.filter(first_name=first_name, last_name=last_name)
        if len(first_name) < 3:
            raise forms.ValidationError('Firstname should be minimum 3 characters!')
        elif first_name.isdigit():
            raise forms.ValidationError('Name must be in letters.')
        else:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError('Lastname should be minimum 3 characters!')
        else:
            return last_name

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Password must match!')
        elif len(password) < 7:
            raise forms.ValidationError('Password should be minimum 7 characters!')
        elif password.isdigit():
            raise forms.ValidationError('Password must contain both letters and numbers!')
        elif password.isalpha():
            raise forms.ValidationError('Password must contain both letters and numbers!')
        else:
            return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email)
        if email_exists.exists():
            raise forms.ValidationError('Email is already taken...Please try another!')
        else:
            return email
