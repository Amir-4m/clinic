from django.apps import AppConfig
from django.conf import settings


class TestimonialsConfig(AppConfig):
    name = 'testimonials'

    def ready(self):
        if getattr(settings, 'TESTIMONIAL_USER_AVATAR_UPLOAD_DIR', None):
            setattr(settings, 'TESTIMONIAL_USER_AVATAR_UPLOAD_DIR', 'testimonial_avatars')
