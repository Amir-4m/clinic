#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.urls import reverse

from .apps import ContactConfig
from .models import Message


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class ContactTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(ContactConfig.name, 'contact')

    def test_get_contact_page(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('contact', kwargs={'is_amp': 'amp/'}))
        self.assertEqual(resp.status_code, 200)

    def test_post_contact_form_by_valid_data(self):
        self.assertEqual(Message.objects.all().count(), 0)
        subject = 'test subject'
        self.client.post(
            reverse('contact'),
            data=dict(
                name='test user',
                email='fake@test.com',
                subject=subject,
                message='test message text'
            )
        )
        self.assertEqual(Message.objects.all().count(), 1)
        self.assertEqual(subject, str(Message.objects.first()))

    def test_post_contact_form_by_invalid_data(self):
        self.assertEqual(Message.objects.all().count(), 0)
        self.client.post(
            reverse('contact'),
            data=dict(
                name='',
                email='',
                subject='',
                message=''
            )
        )
        self.assertEqual(Message.objects.all().count(), 0)
