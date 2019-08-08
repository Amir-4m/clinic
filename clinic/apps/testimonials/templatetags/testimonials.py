#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.template import Library
from django.utils.safestring import mark_safe
from django.conf import settings

from ..services import TestimonialService

register = Library()


@register.simple_tag
def testimonials_css_tags(is_amp=False, bg_image=False):
    testimonials = TestimonialService.get_active_testimonials()
    styles = ''
    for i, item in enumerate(testimonials):
        styles += '''
        .testimonial-slider .swiper-pagination-bullet:nth-of-type({}) {{
            background: url({});
            background-size: cover;
        }}
        '''.format(i + 1, item.user_avatar.url)

    if bg_image:
        styles += '''
        .testimonial-section::before {{
            background: url({}) no-repeat right center;
            background-size: cover;
        }}
        '''.format(bg_image)

    return mark_safe('''
        <link rel="stylesheet" href="{}testimonials/css/testimonials.css">
        <style>{}</style>
        '''.format(settings.STATIC_URL, styles))


@register.simple_tag
def testimonials_js_tags(is_amp=False):
    if is_amp:
        return mark_safe(
            '<script async custom-element="amp-testimonials" '
            'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
        )
    return mark_safe(
        '<script lang="javascript" src="{}testimonials/js/testimonials.js"></script>'.format(
            settings.STATIC_URL
        )
    )


@register.inclusion_tag('testimonials/testimonial-base.html')
def testimonials(is_amp=False):
    return {
        'testimonials': TestimonialService.get_active_testimonials(),
        'is_amp': is_amp
    }
