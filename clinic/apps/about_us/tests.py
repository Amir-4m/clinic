#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.urls import reverse

from .apps import AboutUsConfig


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class AboutUsTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(AboutUsConfig.name, 'about_us')

    def test_get_about_us_page(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('about', kwargs={'is_amp': 'amp'}))
        self.assertEqual(resp.status_code, 200)
