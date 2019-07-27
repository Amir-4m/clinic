from django.test import TestCase
from django.urls import reverse

from .apps import ServicesConfig


class ServicesTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(ServicesConfig.name, 'services')

    def test_get_services_page(self):
        resp = self.client.get(reverse('services'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('services', kwargs={'amp': 'amp'}))
        self.assertEqual(resp.status_code, 200)
