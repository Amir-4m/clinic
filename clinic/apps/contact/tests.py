from django.test import TestCase
from django.urls import reverse

from .apps import ContactConfig


class ContactTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(ContactConfig.name, 'contact')

    def test_get_contact_page(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('contact', kwargs={'amp': 'amp'}))
        self.assertEqual(resp.status_code, 200)
