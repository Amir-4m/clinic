#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .services import ArticlesService, DescriptionTabService


def show_services(request, is_amp=False):
    context = {
        'page': 'services',
        'extend_header': True,
        'articles': ArticlesService.get_articles(),
        'descriptions_tabs': DescriptionTabService.get_descriptions_tabs(),

        'title': _('Services'),
        'descriptions': _('Clinic Services'),
        'is_amp': is_amp
    }

    full_path = request.get_full_path()
    params = ''
    if '?' in full_path:
        params = full_path.split('?', 1)[-1]
    if is_amp:
        context.update(
            canonical_url='{}{}{}'.format(
                reverse('services'), '?' if params else '', params
            )
        )
    else:
        context.update(
            amphtml_url='{}{}{}'.format(
                reverse('services', kwargs={'is_amp': 'amp/'}), '?' if params else '', params
            )
        )

    return render(
        request,
        'services/amp/services.html' if is_amp else 'services/services.html',
        context
    )
