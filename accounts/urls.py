from django.conf.urls import url, include
from accounts.views import logout, login, register
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^password-reset/', include(url_reset))  # urls for password reset
]
