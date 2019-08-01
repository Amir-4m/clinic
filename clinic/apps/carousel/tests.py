import os
import uuid

from PIL import Image
import bs4
from django.core.files import File
from django.conf import settings
from django.test import TestCase
from django.template import Context, Template

from .services import CarouselService
from .apps import CarouselConfig


class CarouselTestCase(TestCase):
    def setUp(self):
        self.carousel_slug = 'carousel-test'
        self.carousel = CarouselService.create_carousel(slug=self.carousel_slug)
        image_file = open(f'{settings.MEDIA_ROOT}/{uuid.uuid4().hex}.png', 'wb+')
        pic = Image.new('RGB', (70, 50))
        pic.save(image_file)
        for i in range(1, 4):
            image_file.seek(0)
            image = File(image_file)
            CarouselService.add_slide(
                self.carousel,
                f'test slide {i}',
                f'test content {i}',
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
                '<link rel="stylesheet" href="/static/carousel/css/carousel.css">'
                '<style>'
                '.slide-bg-0 {'
                f'background-image: url({self.carousel.slides.all()[0].image.url});'
                '}'
                '.slide-bg-1 {'
                f'background-image: url({self.carousel.slides.all()[1].image.url});'
                '}'
                '.slide-bg-2 {'
                f'background-image: url({self.carousel.slides.all()[2].image.url});'
                '}'
                '</style>'
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
                '<style>'
                '.slide-bg-0 {'
                f'background-image: url({self.carousel.slides.all()[0].image.url});'
                'background-size: cover;'
                'background-position: center;'
                '}'
                '.slide-bg-1 {'
                f'background-image: url({self.carousel.slides.all()[1].image.url});'
                'background-size: cover;'
                'background-position: center;'
                '}'
                '.slide-bg-2 {'
                f'background-image: url({self.carousel.slides.all()[2].image.url});'
                'background-size: cover;'
                'background-position: center;'
                '}'
                '</style>'
            )
        )

    def test_carousel_carousel_template_tag(self):
        context = Context({'carousel': self.carousel})
        template = Template('{% load carousel %}{% carousel carousel %}')
        carousel_html = template.render(context)
        doc = bs4.BeautifulSoup(carousel_html)
        self.assertEqual(len(doc.select('.swiper-slide.hero-content-wrap')), 3)
