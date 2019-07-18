from django.shortcuts import render

from clinic.apps.carousel.services import CarouselService


def home(request):
    header_carousel = CarouselService.get_carousel_by_slug('home_header_carousel')
    return render(
        request,
        'clinic/layout.html',
        {
            'extend_header': True,
            'header_carousel': header_carousel
        }
    )
