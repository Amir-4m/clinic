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
        styles += f"""
        .testimonial-slider .swiper-pagination-bullet:nth-of-type({i + 1}) {{
            background: url({item.user_avatar.url});
            background-size: cover;
        }}
        """

    if bg_image:
        styles += f'''
        .testimonial-section::before {{
            background: url({bg_image}) no-repeat right center;
            background-size: cover;
        }}
        '''

    return mark_safe(f'''
        <link rel="stylesheet" href="{ settings.STATIC_URL }testimonials/css/testimonials.css">
        <style>{ styles }</style>
    ''')


@register.simple_tag
def testimonials_js_tags(is_amp=False):
    if is_amp:
        return mark_safe(
            f'<script async custom-element="amp-testimonials" '
            'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
        )
    return mark_safe(
        f'<script lang="javascript" src="{settings.STATIC_URL}testimonials/js/testimonials.js"></script>'
    )


@register.inclusion_tag('testimonials/testimonial-base.html')
def testimonials(is_amp=False):
    return {
        'testimonials': TestimonialService.get_active_testimonials(),
        'is_amp': is_amp
    }
