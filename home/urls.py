from django.conf.urls import url, include
from .views import index, about_view, contact_view, glossary_view, privacy_view, terms_view, faqs_view

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about_view, name='about'),
    url(r'^contact/$', contact_view, name='contact'),
    url(r'^glossary/$', glossary_view, name='glossary'),
    url(r'^privacy/$', privacy_view, name='privacy'),
    url(r'^terms/$', terms_view, name='terms'),
    url(r'^faqs/$', faqs_view, name='faqs'),
]
