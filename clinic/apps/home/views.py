from django.shortcuts import render
from django.conf import settings

from clinic.apps.carousel.services import CarouselService


def home(request, is_amp=False):
    header_carousel = CarouselService.get_carousel_by_slug('home_header_carousel')
    return render(
        request,
        'home/amp/home.html' if is_amp else 'home/home.html',
        {
            'page': 'home',
            'extend_header': True,
            'header_carousel': header_carousel,
            'testimonials_bg_image': f'{settings.STATIC_URL}site/images/theme/testimonial-bg.jpg',
            'departmentsbox_bg_image': f'{settings.STATIC_URL}site/images/theme/departments-bg.jpg',
        }
    )
