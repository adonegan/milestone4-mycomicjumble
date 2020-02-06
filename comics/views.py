from django.shortcuts import render
from .models import Comic


def all_comics(request):
    comics = Comic.objects.all()
    return render(request, "comics.html", {"comics": comics})
