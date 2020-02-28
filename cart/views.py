from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    A view to show cart page
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Logic for adding items to cart
    """
    quantity = 1

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('comics'))


def remove_from_cart(request, id):
    """
    Logic for how to remove items from cart
    """

    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
