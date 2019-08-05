#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.urls.converters import StringConverter


class AMPConverter(StringConverter):
    regex = 'amp'
