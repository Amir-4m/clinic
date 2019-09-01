#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .services import AboutUsService


def show_about(request, is_amp=False):
    context = {
        'page': 'About us',
        'extend_header': True,
        'history': AboutUsService.get_history(),
        'faqs': AboutUsService.get_faqs(),
        'stuffs': AboutUsService.get_stuffs(),
        'members': AboutUsService.get_clinic_team_members(),

        'title': _('About us'),
        'descriptions': _('Clinic About us'),
        'is_amp': is_amp
    }

    full_path = request.get_full_path()
    params = ''
    if '?' in full_path:
        params = full_path.split('?', 1)[-1]
    if is_amp:
        context.update(
            canonical_url='{}{}{}'.format(
                reverse('about'), '?' if params else '', params
            )
        )
    else:
        context.update(
            amphtml_url='{}{}{}'.format(
                reverse('about', kwargs={'is_amp': 'amp'}), '?' if params else '', params
            )
        )

    return render(
        request, 'about_us/amp/about_us.html' if is_amp else 'about_us/about_us.html', context
    )
