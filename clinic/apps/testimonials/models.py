#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from fancy_imagefield.fields import ImageField
from fancy_imagefield.validators import MaxSizeValidator


class Testimonial(models.Model):
    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    user_full_name = models.CharField(max_length=140, verbose_name=_('User Full Name'))
    user_avatar = ImageField(
        validators=[MaxSizeValidator(1024 * 512)],
        upload_to='testimonial_avatars',
        verbose_name=_('User Avatar')
    )
    location = models.CharField(max_length=100, verbose_name=_('Location'))
    text = RichTextField(verbose_name=_('Text'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="48">'.format(self.user_avatar.url))

    def __str__(self):
        return self.user_full_name
