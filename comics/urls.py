from django.conf.urls import url, include
from .views import all_comics, detail

urlpatterns = [
    url(r'^$', all_comics, name='comics'),
    url(r'(?P<comic_id>\d+)/$', detail, name='detail')
]
