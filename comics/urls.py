from django.conf.urls import url, include
from .views import all_comics

urlpatterns = [
    url(r'^$', all_comics, name='comics'),
]