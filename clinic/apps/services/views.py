#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render

from .services import ArticlesService, DescriptionTabService


def show_services(request, is_amp=False):
    return render(
        request,
        'services/amp/services.html' if is_amp else 'services/services.html',
        {
            'page': 'services',
            'extend_header': True,
            'articles': ArticlesService.get_articles(),
            'descriptions_tabs': DescriptionTabService.get_descriptions_tabs()
        }
    )
