from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm


def index(request):
    """A view for the default homepage"""
    return render(request, "index.html")


def about_view(request):
    """A view that displays the about page"""
    return render(request, "about.html")


def contact_view(request):
    """A view that displays the contact page"""
    contact_form = ContactForm
    return render(request, "contact.html", {'form': contact_form})


def glossary_view(request):
    """A view that displays the glossary page"""
    return render(request, "glossary.html")


def privacy_view(request):
    """A view that displays the privacy page"""
    return render(request, "privacy.html")


def terms_view(request):
    """A view that displays the terms and conditions page"""
    return render(request, "terms.html")


def faqs_view(request):
    """A view that displays the faqs page"""
    return render(request, "faqs.html")
