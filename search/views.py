from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comics.models import Comic


def do_search(request):
    comics_list = Comic.objects.all()
    query = request.GET.get('q')
    if query:
        comics_list = Comic.objects.filter(
            Q(name__icontains=query) | Q(grade__icontains=query) |
            Q(brand__icontains=query)
        ).distinct()
    paginator = Paginator(comics_list, 4)

    page = request.GET.get('page')
    try:
        comics = paginator.page(page)
    except PageNotAnInteger:

        comics = paginator.page(1)
    except EmptyPage:

        comics = paginator.page(paginator.num_pages)
    return render(request, "search.html", {"comics": comics})
