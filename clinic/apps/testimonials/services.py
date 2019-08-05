#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .models import Testimonial


class TestimonialService(object):
    @staticmethod
    def get_active_testimonials():
        return Testimonial.objects.filter(is_active=True)
