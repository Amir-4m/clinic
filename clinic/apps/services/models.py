#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from fancy_imagefield.fields import ImageField
from fancy_imagefield.validators import MaxSizeValidator


class Article(models.Model):
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    title = models.CharField(max_length=80, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    read_more_link = models.URLField(blank=True, null=True, verbose_name=_('Read More Link'))

    def __str__(self):
        return self.title


class DescriptionTab(models.Model):
    class Meta:
        verbose_name = _('Description Tab')
        verbose_name_plural = _('Description Tabs')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    name = models.CharField(max_length=40, verbose_name=_('Name'))  # Show as tab text
    title = models.CharField(max_length=120, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = ImageField(validators=[MaxSizeValidator(1024)], verbose_name=_('Image'))

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="48">'.format(self.image.url))

    @property
    def detail_preview(self):
        return mark_safe('<img src="{}" width="320">'.format(self.image.url))

    def __str__(self):
        return '{} - {}'.format(self.name, self.title)
