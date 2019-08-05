#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class Message(models.Model):
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    message = RichTextField(verbose_name=_('Message'))

    def __str__(self):
        return self.subject
