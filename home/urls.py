from django.conf.urls import url, include
from .views import index, about_view, contact_view, glossary_view

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about_view, name='about'),
    url(r'^contact/$', contact_view, name='contact'),
    url(r'^glossary/$', glossary_view, name='glossary'),
]
