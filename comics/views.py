from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comic


def all_comics(request):
    """Show all comics but paginate after eight comics display on page"""
    comics_list = Comic.objects.all()
    paginator = Paginator(comics_list, 8)

    page = request.GET.get('page')
    try:
        comics = paginator.page(page)
    except PageNotAnInteger:

        comics = paginator.page(1)
    except EmptyPage:

        comics = paginator.page(paginator.num_pages)
    return render(request, "comics.html", {"comics": comics})


def detail(request, comic_id):
    """Function view for comic details page"""
    comic = Comic.objects.get(pk=comic_id)
    return render(request, "details.html", {"comic": comic})
