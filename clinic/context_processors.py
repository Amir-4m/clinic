#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings


def global_settings(request):
    return {'IRAN_YEKAN_LICENSE': getattr(settings, 'IRAN_YEKAN_LICENSE')}
