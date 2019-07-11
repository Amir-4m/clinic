#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from django.contrib import admin

from . import urlpatterns

admin.autodiscover()

urlpatterns += [
    path(
        'robots.txt',
        TemplateView.as_view(template_name="robots-block.txt", content_type="text/plain"),
        name='robots'
    ),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('django_contrib.recaptcha.urls', namespace='recaptcha')),
    # Django Admin
    path('', admin.site.urls),
]
