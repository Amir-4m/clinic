#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
import uuid
from unittest import skipIf

from PIL import Image
import bs4
from django.core.files import File
from django.conf import settings
from django.test import TestCase
from django.template import Context, Template

from .services import CarouselService
from .apps import CarouselConfig


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class CarouselTestCase(TestCase):
    def setUp(self):
        self.carousel_slug = 'carousel-test'
        self.carousel = CarouselService.create_carousel(slug=self.carousel_slug)
        image_file = open(
            '{}/{}.png'.format(settings.MEDIA_ROOT, uuid.uuid4().hex), 'wb+'
        )
        pic = Image.new('RGB', (70, 50))
        pic.save(image_file)
        for i in range(1, 4):
            image_file.seek(0)
            image = File(image_file)
            CarouselService.add_slide(
                self.carousel,
                'test slide %d' % i,
                'test content %d' % i,
                image,
                None,
                priority=3 - i
            )
        self.image_file = image_file.name

    def tearDown(self):
        os.remove(self.image_file)

    def test_carousel_appconfig(self):
        self.assertEqual(CarouselConfig.name, 'carousel')

    def test_get_carousel_by_slug(self):
        self.assertEqual(
            self.carousel, CarouselService.get_carousel_by_slug(self.carousel_slug)
        )

        self.assertEqual(
            None, CarouselService.get_carousel_by_slug('not-found-slug')
        )

    def test_carousel_js_template_tags(self):
        context = Context({})

        template = Template('{% load carousel %}{% carousel_js_tags %}')
        jstag = template.render(context)
        self.assertEqual(
            jstag, '<script lang="javascript" src="/static/carousel/js/carousel.js"></script>'
        )

    def test_carousel_js_template_tags_for_amp(self):
        context = Context({})

        template = Template('{% load carousel %}{% carousel_js_tags is_amp=True %}')
        jstag = template.render(context)
        self.assertEqual(
            jstag,
            (
                '<script async custom-element="amp-carousel" '
                'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
            )
        )

    def test_carousel_css_template_tags(self):
        context = Context()

        template = Template(r'{% load carousel %}{% carousel_css_tags %}')
        csstag = template.render(context)
        self.assertEqual(
            csstag.replace('       ', '').replace('\n', '').strip(),
            '<link rel="stylesheet" href="/static/carousel/css/carousel.css">'
        )

        context = Context({'carousel': self.carousel})
        template = Template(r'{% load carousel %}{% carousel_css_tags carousel=carousel %}')
        csstag = template.render(context)
        self.assertEqual(
            csstag.replace('    ', '').replace('\n', '').strip(),
            (
                (
                    '<link rel="stylesheet" href="/static/carousel/css/carousel.css">'
                    '<style>'
                    '.slide-bg-0 {'
                    'background-image: url({});'
                    '}'
                    '.slide-bg-1 {'
                    'background-image: url({});'
                    '}'
                    '.slide-bg-2 {'
                    'background-image: url({});'
                    '}'
                    '</style>'
                ).format(*[s.image.url for s in self.carousel.slides.all()])
            )
        )

    def test_carousel_css_template_tags_for_amp(self):
        context = Context()
        template = Template(r'{% load carousel %}{% carousel_css_tags is_amp=True %}')
        csstag = template.render(context)
        self.assertEqual(
            csstag.replace('       ', '').replace('\n', '').strip(), ''
        )

        context = Context({'carousel': self.carousel})
        template = Template(r'{% load carousel %}{% carousel_css_tags carousel=carousel is_amp=True %}')
        csstag = template.render(context)

        self.assertEqual(
            csstag.replace('    ', '').replace('\n', '').strip(),
            (
                (
                    '<style>'
                    '.slide-bg-0 {'
                    'background-image: url({});'
                    'background-size: cover;'
                    'background-position: center;'
                    '}'
                    '.slide-bg-1 {'
                    'background-image: url({});'
                    'background-size: cover;'
                    'background-position: center;'
                    '}'
                    '.slide-bg-2 {'
                    'background-image: url({});'
                    'background-size: cover;'
                    'background-position: center;'
                    '}'
                    '</style>'
                ).format([s.image.url for s in self.carousel.slides.all()])
            )
        )

    def test_carousel_carousel_template_tag(self):
        context = Context({'carousel': self.carousel})
        template = Template('{% load carousel %}{% carousel carousel %}')
        carousel_html = template.render(context)
        doc = bs4.BeautifulSoup(carousel_html)
        self.assertEqual(len(doc.select('.swiper-slide.hero-content-wrap')), 3)
