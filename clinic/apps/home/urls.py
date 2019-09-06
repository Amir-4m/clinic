#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.urls import re_path

from .views import home


urlpatterns = [
    re_path(r'^(?P<is_amp>amp)?/?$', home, name="home"),
]
