#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from fancy_imagefield.fields import ImageField
from fancy_imagefield.validators import MaxSizeValidator


class Carousel(models.Model):
    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.slug


class Slide(models.Model):
    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        ordering = ['priority']

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    content = RichTextField(verbose_name=_('Content'))
    details_link = models.URLField(null=True, blank=True, verbose_name=_('Details Link'))
    priority = models.IntegerField(verbose_name=_('Priority'))
    image = ImageField(
        validators=[MaxSizeValidator(1024)], upload_to="carousels_slides", verbose_name=_('Image')
    )
    carousel = models.ForeignKey(
        Carousel, related_name='slides', on_delete=models.CASCADE, verbose_name=_('Carousel')
    )

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="48">'.format(self.image.url))

    @property
    def detail_preview(self):
        return mark_safe('<img src="{}" width="320">'.format(self.image.url))

    def __str__(self):
        return self.title
