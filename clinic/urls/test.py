#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from django.contrib import admin

from . import urlpatterns
from .worker import urlpatterns as worker_urlpatterns  # noqa
from .web import urlpatterns as web_urlpatterns  # noqa
from .panel import urlpatterns as panel_urlpatterns  # noqa


admin.autodiscover()

urlpatterns += [
    path(r'about/', include('clinic.apps.about_us.urls')),
    path(r'services/', include('clinic.apps.services.urls')),
    path(r'contact/', include('clinic.apps.contact.urls')),
    path(r'', include('clinic.apps.home.urls')),
    # Sub Apps URLs
    path(
        'robots.txt',
        TemplateView.as_view(template_name="robots-block.txt", content_type="text/plain"),
        name='robots'
    ),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
