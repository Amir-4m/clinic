from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def carousel_js_tags(is_amp=False):
    if is_amp:
        return mark_safe(
            f'<script async custom-element="amp-carousel" '
            'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
        )
    return mark_safe(
        f'<script lang="javascript" src="{settings.STATIC_URL}carousel/js/carousel.js"></script>'
    )


@register.simple_tag
def carousel_css_tags(carousel=None, is_amp=False):
    image_styles = ''
    extra_styles = ''
    if is_amp:
        extra_styles = f'''
                background-size: cover;
                background-position: center;
        '''

    if carousel:
        for index, slide in enumerate(carousel.slides.all()):
            image_styles += f'''
            .slide-bg-{index} {{
                background-image: url({slide.image.url});
                {extra_styles}
            }}
            '''

    image_styles = f'<style>\n{image_styles}\n</style>' if image_styles else ''
    if is_amp:
        return mark_safe(image_styles)

    return mark_safe(
        f'''
        <link rel="stylesheet" href="{settings.STATIC_URL}carousel/css/carousel.css">
        {image_styles}
        '''
    )


@register.inclusion_tag('carousel/carousel-base.html')
def carousel(carousel, is_amp=False):
    return {
        'carousel': carousel,
        'is_amp': is_amp
    }
