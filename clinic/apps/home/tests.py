from django.test import TestCase
from django.urls import reverse

from .apps import HomeConfig


class HomeTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(HomeConfig.name, 'home')

    def test_get_home_page(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('home', kwargs={'amp': 'amp'}))
        self.assertEqual(resp.status_code, 200)
