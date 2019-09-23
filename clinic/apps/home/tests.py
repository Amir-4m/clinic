#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.urls import reverse

from .apps import HomeConfig


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class HomeTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(HomeConfig.name, 'home')

    def test_get_home_page(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('home', kwargs={'is_amp': 'amp/'}))
        self.assertEqual(resp.status_code, 200)
