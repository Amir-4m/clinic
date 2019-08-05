#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['created']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = _('Name')
        self.fields['email'].widget.attrs['placeholder'] = _('E-mail')
        self.fields['subject'].widget.attrs['placeholder'] = _('Subject')
        self.fields['message'].widget.attrs['placeholder'] = _('message')
