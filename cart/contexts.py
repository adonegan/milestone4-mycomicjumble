from django.shortcuts import get_object_or_404
from comics.models import Comic


def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    comic_count = 0

    for id, quantity in cart.items():
        comic = get_object_or_404(Comic, pk=id)
        total += quantity * comic.price
        comic_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'comic': comic})

    return {'cart_items': cart_items, 'total': total, 'comic_count': comic_count}
