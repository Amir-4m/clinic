from .models import Testimonial


class TestimonialService(object):
    @staticmethod
    def get_active_testimonials():
        return Testimonial.objects.filter(is_active=True)
