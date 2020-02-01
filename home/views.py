from django.shortcuts import render


def index(request):
    """A view for the default homepage"""
    return render(request, "index.html")
