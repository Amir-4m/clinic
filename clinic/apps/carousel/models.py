from django.db import models
from django.utils.translation import ugettext as _


class Carousel(models.Model):
    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')

    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


class Slide(models.Model):
    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        ordering = ['priority']

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    details_link = models.URLField(null=True, blank=True)
    priority = models.IntegerField()
    image = models.ImageField(upload_to="carousels_slides")
    carousel = models.ForeignKey(
        Carousel, related_name='slides', on_delete=models.CASCADE
    )
