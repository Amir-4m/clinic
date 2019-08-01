from django.test import TestCase
from django.urls import reverse

from .apps import AboutUsConfig


class AboutUsTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(AboutUsConfig.name, 'about_us')

    def test_get_about_us_page(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('about', kwargs={'amp': 'amp'}))
        self.assertEqual(resp.status_code, 200)
