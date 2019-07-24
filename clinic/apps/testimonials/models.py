from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Testimonial(models.Model):
    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    created_at = models.DateTimeField(auto_now_add=True)
    user_full_name = models.CharField(max_length=140)
    user_avatar = models.ImageField(
        upload_to=getattr(settings, 'TESTIMONIAL_USER_AVATAR_UPLOAD_DIR', 'testimonial_avatars')
    )
    location = models.CharField(max_length=100)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
