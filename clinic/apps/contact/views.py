#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.urls import reverse

from .forms import MessageForm


def show_contact(request, is_amp=False):
    form = MessageForm()
    message = ''
    if request.method.lower() == 'post':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = _('Your message registered successfuly')
            form.save()
            form = MessageForm()

    context = {
        'page': 'Contact',
        'extend_header': True,
        'form': form,

        'title': _('Contact'),
        'descriptions': _('Clinic Contact'),
        'is_amp': is_amp
    }

    full_path = request.get_full_path()
    params = ''
    if '?' in full_path:
        params = full_path.split('?', 1)[-1]
    if is_amp:
        context.update(
            canonical_url='{}{}{}'.format(
                reverse('contact'), '?' if params else '', params
            )
        )
    else:
        context.update(
            amphtml_url='{}{}{}'.format(
                reverse('contact', kwargs={'is_amp': 'amp/'}), '?' if params else '', params
            )
        )

    context['message'] = message
    context['recaptcha_v3_action'] = settings.RECAPTCHA_V3_ACTION
    context['recaptcha_v3_site_key'] = settings.RECAPTCHA_V3_SITE_KEY

    return render(
        request, 'contact/amp/contact.html' if is_amp else 'contact/contact.html', context
    )
