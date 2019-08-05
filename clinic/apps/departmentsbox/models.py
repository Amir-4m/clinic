#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from fancy_imagefield.fields import ImageField
from fancy_imagefield.validators import MaxSizeValidator


class Department(models.Model):
    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    descriptions = models.CharField(max_length=250, verbose_name=_('Descriptions'))
    logo = ImageField(
        validators=[MaxSizeValidator(256)], upload_to='department_logos', verbose_name=_('Logo')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    @property
    def preview(self):
        return mark_safe('<img src="{}">'.format(self.logo.url))

    def __str__(self):
        return self.title
