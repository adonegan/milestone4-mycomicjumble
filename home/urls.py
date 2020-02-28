from django.conf.urls import url, include
from .views import index, about_view, glossary_view, privacy_view, terms_view, faqs_view

urlpatterns = [
    url(r'^index/$', index, name='index'),  # so visitors can access each page
    url(r'^about/$', about_view, name='about'),
    url(r'^glossary/$', glossary_view, name='glossary'),
    url(r'^privacy/$', privacy_view, name='privacy'),
    url(r'^terms/$', terms_view, name='terms'),
    url(r'^faqs/$', faqs_view, name='faqs'),
]
