"""mycomicjumble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from home import urls as urls_home
from home.views import index, about_view
from comics import urls as urls_comics
from comics.views import all_comics, detail
from search import urls as urls_search
from search.views import do_search
from cart import urls as urls_cart
from cart.views import view_cart, add_to_cart
from accounts.views import logout, login, register
from accounts import urls as accounts_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^about/', about_view, name='about'),
    url(r'^comics/', include(urls_comics), name='comics'),
    url(r'^search/', include(urls_search), name='search'),
    url(r'^cart/', include(urls_cart)),
    url(r'^comics/details/(?P<comic_id>[0-12]+)', detail, name='detail'),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', register, name="register"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
