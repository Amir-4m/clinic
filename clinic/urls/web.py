#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.urls import register_converter, path, include
from django.views.generic import TemplateView

from . import urlpatterns
from .converters import AMPConverter

register_converter(AMPConverter, 'amp')

urlpatterns += [
    path(r'about/', include('clinic.apps.about_us.urls')),
    path(r'services/', include('clinic.apps.services.urls')),
    path(r'contact/', include('clinic.apps.contact.urls')),
    path(r'', include('clinic.apps.home.urls')),
    path(
        'robots.txt',
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name='robots'
    ),
    path('amp/', include('django_contrib.amp.urls', namespace='amp')),
]
