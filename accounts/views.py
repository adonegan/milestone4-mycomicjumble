from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect(reverse('index'))
