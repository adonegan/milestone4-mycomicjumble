from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm


def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect(reverse('index'))


def login(request):
    login_form = LoginForm
    return render(request, 'login.html', {'login_form': login_form})
