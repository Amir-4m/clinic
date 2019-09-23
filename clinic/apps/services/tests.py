#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.urls import reverse
from django.utils.safestring import mark_safe

from .apps import ServicesConfig
from .models import Article, DescriptionTab


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class ServicesTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(ServicesConfig.name, 'services')

    def test_get_services_page(self):
        resp = self.client.get(reverse('services'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('services', kwargs={'is_amp': 'amp/'}))
        self.assertEqual(resp.status_code, 200)

    def test_article_string(self):
        article = Article.objects.first()
        self.assertEqual(article.title, str(article))

    def test_descriptiontab_string(self):
        descriptiontab = DescriptionTab.objects.first()
        dt_str = '{} - {}'.format(
            descriptiontab.name, descriptiontab.title
        )
        self.assertEqual(dt_str, str(descriptiontab))

    def test_descriptiontab_preview(self):
        descriptiontab = DescriptionTab.objects.first()
        self.assertEqual(
            descriptiontab.preview,
            mark_safe('<img src="{}" width="48">'.format(descriptiontab.image.url))
        )
