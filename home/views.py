from django.shortcuts import render
from django.conf import settings


def index(request):
    """A view for the default homepage"""
    return render(request, "index.html")


def about_view(request):
    """A view that displays the about page"""
    return render(request, "about.html")
