#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path

from .views import home


urlpatterns = [
    path(r'', home, name="home"),
]
