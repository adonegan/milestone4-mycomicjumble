from django.shortcuts import render, redirect, reverse


def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, id):
    quantity = 1

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def remove_from_cart(request, id):

    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
