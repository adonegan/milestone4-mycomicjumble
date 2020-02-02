from django.conf.urls import url, include
from .views import index, about_view

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about_view, name='about'),
]
