#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def carousel_js_tags(is_amp=False):
    if is_amp:
        return mark_safe(
            '<script async custom-element="amp-carousel" '
            'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
        )
    return mark_safe(
        '<script lang="javascript" src="{}carousel/js/carousel.js"></script>'.format(
            settings.STATIC_URL
        )
    )


@register.simple_tag
def carousel_css_tags(carousel=None, is_amp=False):
    image_styles = ''
    extra_styles = ''
    if is_amp:
        extra_styles = '''
                background-size: cover;
                background-position: center;
        '''

    if carousel:
        for index, slide in enumerate(carousel.slides.all()):
            image_styles += '''
            .slide-bg-{} {{
                background-image: url({});
                {}
            }}
            '''.format(
                index, slide.image.url, extra_styles
            )

    image_styles = '<style>\n{}\n</style>'.format(image_styles) if image_styles else ''
    if is_amp:
        return mark_safe(image_styles)

    return mark_safe(
        '''
        <link rel="stylesheet" href="{}carousel/css/carousel.css">
        {}
        '''.format(
            settings.STATIC_URL, image_styles
        )
    )


@register.inclusion_tag('carousel/carousel-base.html')
def carousel(carousel, is_amp=False):
    return {
        'carousel': carousel,
        'is_amp': is_amp
    }
