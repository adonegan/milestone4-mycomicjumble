from django.shortcuts import render
from django.db.models import Q
from comics.models import Comic


def do_search(request):
    comics_list = Comic.objects.all()
    query = request.GET.get('q')
    if query:
        comics_list = Comic.objects.filter(
            Q(name__icontains=query) | Q(grade__icontains=query) |
            Q(brand__icontains=query)
        ).distinct()

    context = {
        'comics': comics_list
    }
    return render(request, "search.html", context)
