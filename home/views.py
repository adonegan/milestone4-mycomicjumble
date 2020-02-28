from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm


def index(request):
    """
    A view to show the Index page - it's
    called Home on front site
    """
    return render(request, "index.html")


def about_view(request):
    """
    A view to show the About page
    """
    return render(request, "about.html")


def contact_view(request):
    """
    A view to show the Contact page and
    to serve form logic so owner can
    receive mail
    """
    contact_form = ContactForm
    return render(request, "contact.html", {'form': contact_form})


def glossary_view(request):
    """
    A view that shows the glossary page
    """
    return render(request, "glossary.html")


def privacy_view(request):
    """
    A view that displays the privacy page
    """
    return render(request, "privacy.html")


def terms_view(request):
    """
    A view that displays the terms and conditions page
    """
    return render(request, "terms.html")


def faqs_view(request):
    """
    A view that displays the faqs page
    """
    return render(request, "faqs.html")
