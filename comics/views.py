from django.shortcuts import render
from .models import Comic


def all_comics(request):
    comics = Comic.objects.all()
    return render(request, "comics.html", {"comics": comics})


def detail(request, comic_id):
    """Function view for comic details page"""
    comic = Comic.objects.get(pk=comic_id)
    return render(request, "details.html", {"comic": comic})
