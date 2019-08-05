#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

from ..services import DepartmentService


register = Library()


@register.simple_tag
def departmentsbox_css_tags(is_amp=None, bg_image=None):
    style = '<link rel="stylesheet" href="{}departmentsbox/css/departmentsbox.css">'.format(
        settings.STATIC_URL
    )
    if bg_image:
        style += '''
        <style>
        .our-departments {{
            background: url({}) no-repeat;
            background-size: cover;
        }}
        </style>
    '''.format(bg_image)
    return mark_safe(style)


@register.inclusion_tag('departmentsbox/departmentsbox-base.html')
def departmentsbox(is_amp=False):
    return dict(
        departments=DepartmentService.get_all_departments(),
        is_amp=is_amp
    )
