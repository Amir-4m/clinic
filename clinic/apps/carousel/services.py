#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import transaction
from django.db.models import F

from .models import Carousel, Slide


class CarouselService(object):
    @staticmethod
    def get_carousel_by_slug(slug):
        try:
            return Carousel.objects.get(slug=slug)
        except Carousel.DoesNotExist:
            pass

    @staticmethod
    def create_carousel(slug):
        return Carousel.objects.create(slug=slug)

    @staticmethod
    def add_slide(carousel, title, content, image, details_link=None, priority=None):
        with transaction.atomic():
            if priority:
                carousel.slides.filter(priority__gte=priority).update(
                    priority=F('priority') + 1
                )
            else:
                priority = carousel.slides.all().count()

            return Slide.objects.create(
                carousel=carousel,
                title=title,
                content=content,
                image=image,
                details_link=details_link,
                priority=priority
            )
