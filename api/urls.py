from django.conf.urls import include, url
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^(?P<pk>\w+)/dj/$', views.SwagEndpoint.as_view(), name='swag_endpoint'),
]
