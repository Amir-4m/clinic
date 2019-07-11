#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.handlers.wsgi import WSGIHandler
from django.test import TestCase, override_settings

from .wsgi import application
from .context_processors import global_settings


class WSGITestCase(TestCase):
    def test_application(self):
        self.assertIsInstance(application, WSGIHandler)


class ContextProcessorsTestCase(TestCase):
    @override_settings(IRAN_YEKAN_LICENSE='LICENSE')
    def test_global_settings(self):
        class MockRequest(object):
            pass

        context = global_settings(MockRequest())
        self.assertEqual(context.get('IRAN_YEKAN_LICENSE'), 'LICENSE')
