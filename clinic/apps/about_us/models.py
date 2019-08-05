#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from fancy_imagefield.fields import ImageField
from fancy_imagefield.validators import MaxSizeValidator


class History(models.Model):
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    text = RichTextField(config_name='basic', verbose_name=_('Text'))
    image = ImageField(validators=[MaxSizeValidator(1024)], verbose_name=_('Image'))
    details_link = models.URLField(blank=True, null=True, verbose_name=_('Details Link'))

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="48">'.format(self.image.url))

    def __str__(self):
        return self.title


class Faq(models.Model):
    class Meta:
        verbose_name = _('Faq')
        verbose_name_plural = _('Faqs')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    question = models.CharField(max_length=100, verbose_name=_('Question'))
    answer = models.CharField(max_length=255, verbose_name=_('Answer'))

    def __str__(self):
        return self.question


class Stuff(models.Model):
    class Meta:
        verbose_name = _('Stuff')
        verbose_name_plural = _('Stuffs')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    logo = ImageField(validators=[MaxSizeValidator(256)], verbose_name=_('Logo'))

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="24">'.format(self.logo.url))

    def __str__(self):
        return self.title


class ClinicTeamMember(models.Model):
    class Meta:
        verbose_name = _('Clinic Team Member')
        verbose_name_plural = _('Clinic Team Members')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    name = models.CharField(max_length=120, verbose_name=_('Name'))
    degree = models.CharField(max_length=80, verbose_name=_('Degree'))
    avatar = ImageField(validators=[MaxSizeValidator(512)], verbose_name=_('Avatar Image'))

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="48">'.format(self.avatar.url))

    def __str__(self):
        return self.name
