#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from clinic.apps.carousel.services import CarouselService


def home(request, is_amp=False):
    header_carousel = CarouselService.get_carousel_by_slug('home_header_carousel')
    context = {
        'page': 'home',
        'extend_header': True,
        'header_carousel': header_carousel,
        'testimonials_bg_image': '{}site/images/theme/testimonial-bg.jpg'.format(
            settings.STATIC_URL
        ),
        'departmentsbox_bg_image': '{}site/images/theme/departments-bg.jpg'.format(
            settings.STATIC_URL
        ),

        'title': _('Home'),
        'descriptions': _('Clinic home page'),
        'is_amp': is_amp
    }
    full_path = request.get_full_path()
    params = ''
    if '?' in full_path:
        params = full_path.split('?', 1)[-1]

    if is_amp:
        context.update(
            canonical_url='{}{}{}'.format(
                reverse('home'), '?' if params else '', params
            )
        )
    else:
        context.update(
            amphtml_url='{}{}{}'.format(
                reverse('home', kwargs={'is_amp': 'amp'}), '?' if params else '', params
            )
        )

    request.get_full_path()
    return render(
        request, 'home/amp/home.html' if is_amp else 'home/home.html', context
    )
