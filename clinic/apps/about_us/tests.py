#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.urls import reverse
from django.utils.safestring import mark_safe

from .apps import AboutUsConfig
from .models import History, Faq, Stuff, ClinicTeamMember


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

    def test_about_us_history_model_to_string_value(self):
        history = History.objects.first()
        self.assertEqual(history.title, str(history))

    def test_about_us_faq_model_to_string_value(self):
        faq = Faq.objects.first()
        self.assertEqual(faq.question, str(faq))

    def test_about_us_stuff_model_to_string_value(self):
        stuff = Stuff.objects.first()
        self.assertEqual(stuff.title, str(stuff))

    def test_about_us_clinicteammember_model_to_string_value(self):
        member = ClinicTeamMember.objects.first()
        self.assertEqual(member.name, str(member))

    def test_about_us_history_model_preview_value(self):
        history = History.objects.first()
        self.assertEqual(
            history.preview,
            mark_safe('<img src="{}" width="48">'.format(history.image.url))
        )

    def test_about_us_stuff_model_preview_value(self):
        stuff = Stuff.objects.first()
        self.assertEqual(
            stuff.preview,
            mark_safe('<img src="{}" width="24">'.format(stuff.logo.url))
        )

    def test_about_us_clinicteammember_model_to_preview_value(self):
        member = ClinicTeamMember.objects.first()
        self.assertEqual(
            member.preview,
            mark_safe('<img src="{}" width="48">'.format(member.avatar.url))
        )
