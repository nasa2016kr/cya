from . import views

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^check$', views.check, name='check'),
    url(r'^about$', views.about, name='about'),
    url(r'^generate_asteroid', views.generate_asteroid, name='generate_asteroid'),
]

