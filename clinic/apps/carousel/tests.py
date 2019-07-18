import os
import uuid

from PIL import Image
import bs4
from django.core.files import File
from django.conf import settings
from django.test import TestCase
from django.template import Context, Template

from .services import CarouselService


class CarouselTestCase(TestCase):
    def setUp(self):
        self.carousel = CarouselService.create_carousel(slug='carousel-test')
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

    def test_carousel_js_template_tags(self):
        context = Context({})

        template = Template('{% load carousel %}{% carousel_js_tags %}')
        jstag = template.render(context)
        self.assertEqual(
            jstag,
            '''
            <script src="/static/carousel/js/swiper.min.js"></script>
            <script>
              swiper = new Swiper('.swiper-container', {
                direction: 'horizontal',
                loop: false,


                navigation: {
                  nextEl: '.swiper-button-next',
                  prevEl: '.swiper-button-prev',
                },

                scrollbar: {
                  el: '.swiper-scrollbar',
                },
              });

              bullets = document.getElementsByClassName('swiper-pagination-bullet');
              for(var i=0; i < bullets.length; i++){
                var bullet = bullets[i];
                bullet.addEventListener('click', function (e) {
                  e.preventDefault();
                  for(var j=0; j < bullets.length; j++){
                    bullets[j].classList.remove('swiper-pagination-bullet-active');
                  }
                  this.classList.add('swiper-pagination-bullet-active');
                  swiper.slideTo(this.getAttribute('data-slide'), 200);
                });
              }
            </script>'''
        )

    def test_carousel_css_template_tags(self):
        context = Context()

        template = Template('{% load carousel %}{% carousel_css_tags %}')
        csstag = template.render(context)
        self.assertEqual(
            csstag,
            '<link rel="stylesheet" href="/static/carousel/css/swiper.min.css">'
        )

    def test_carousel_carousel_template_tag(self):
        context = Context({'carousel': self.carousel})
        template = Template('{% load carousel %}{% carousel carousel %}')
        carousel_html = template.render(context)
        doc = bs4.BeautifulSoup(carousel_html)
        self.assertEqual(len(doc.select('.swiper-slide.hero-content-wrap')), 3)
