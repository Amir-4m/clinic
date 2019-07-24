from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

from ..services import DepartmentService


register = Library()


@register.simple_tag
def departmentsbox_css_tags(is_amp=None, bg_image=None):
    style = f'<link rel="stylesheet" href="{settings.STATIC_URL}departmentsbox/css/departmentsbox.css">'
    if bg_image:
        style += f'''
        <style>
        .our-departments {{
            background: url({bg_image}) no-repeat;
            background-size: cover;
        }}
        </style>
    '''
    return mark_safe(style)


@register.inclusion_tag('departmentsbox/departmentsbox-base.html')
def departmentsbox(is_amp=False, bg_image=None):
    return dict(
        departments=DepartmentService.get_all_departments(),
        is_amp=is_amp
    )
