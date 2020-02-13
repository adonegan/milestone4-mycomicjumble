from django.shortcuts import render, redirect, reverse


def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, comic_id):
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id])

    request.session['cart'] = cart
    return redirect(reverse('index'))
