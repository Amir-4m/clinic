#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from django.test import TestCase
from django.conf import settings
from django.template import Template, Context

from .apps import TestimonialsConfig
from .services import TestimonialService


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class TestimonialsTestCase(TestCase):
    def setUp(self):
        self.testimonials = TestimonialService.get_active_testimonials()

    def tearDown(self):
        pass

    def test_app_config(self):
        self.assertEqual(TestimonialsConfig.name, 'testimonials')

    def test_testimonials_css_tags(self):
        context = Context()
        template = Template(r'{% load testimonials %}{% testimonials_css_tags %}')
        styles = template.render(context)
        self.assertEqual(
            styles.replace('    ', '').strip(),
            '''
                <link rel="stylesheet" href="/static/testimonials/css/testimonials.css">
                <style>
                .testimonial-slider .swiper-pagination-bullet:nth-of-type(1) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(2) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(3) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(4) {{
                    background: url({});
                    background-size: cover;
                }}
                </style>
            '''.format(t.user_avatar.url for t in self.testimonials).replace('    ', '').strip()
        )

        context = Context()
        template = Template(r'{% load testimonials %}{% testimonials_css_tags bg_image="x/y/z.png" %}')
        styles = template.render(context)
        self.assertEqual(
            styles.replace('    ', '').strip(),
            '''
            <link rel="stylesheet" href="/static/testimonials/css/testimonials.css">
            <style>
            .testimonial-slider .swiper-pagination-bullet:nth-of-type(1) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(2) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(3) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(4) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-section::before {{
                background: url(x/y/z.png) no-repeat right center;
                background-size: cover;
            }}
            </style>
            '''.format(*[t.user_avatar.url for t in self.testimonials]).replace('    ', '').strip()
        )

    def test_testimonials_css_tags_for_amp(self):
        context = Context()
        template = Template(r'{% load testimonials %}{% testimonials_css_tags is_amp=True %}')
        styles = template.render(context)
        self.assertEqual(
            styles.replace('    ', '').strip(),
            '''
                <link rel="stylesheet" href="/static/testimonials/css/testimonials.css">
                <style>
                .testimonial-slider .swiper-pagination-bullet:nth-of-type(1) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(2) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(3) {{
                    background: url({});
                    background-size: cover;
                }}

                .testimonial-slider .swiper-pagination-bullet:nth-of-type(4) {{
                    background: url({});
                    background-size: cover;
                }}
                </style>
            '''.format(*[t.user_avatar.url for t in self.testimonials]).replace('    ', '').strip()
        )

        context = Context()
        template = Template(
            r'{% load testimonials %}{% testimonials_css_tags is_amp=True bg_image="x/y/z.png" %}'
        )
        styles = template.render(context)
        self.assertEqual(
            styles.replace('    ', '').strip(),
            '''
            <link rel="stylesheet" href="/static/testimonials/css/testimonials.css">
            <style>
            .testimonial-slider .swiper-pagination-bullet:nth-of-type(1) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(2) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(3) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-slider .swiper-pagination-bullet:nth-of-type(4) {{
                background: url({});
                background-size: cover;
            }}

            .testimonial-section::before {{
                background: url(x/y/z.png) no-repeat right center;
                background-size: cover;
            }}
            </style>
            '''.format(*[t.user_avatar.url for t in self.testimonials]).replace('    ', '').strip()
        )

    def test_get_js_tags(self):
        context = Context()
        template = Template(
            r'{% load testimonials %}{% testimonials_js_tags %}'
        )
        jstag = template.render(context)
        self.assertEqual(
            jstag,
            '<script lang="javascript" src="{}testimonials/js/testimonials.js"></script>'.format(
                settings.STATIC_URL
            )
        )

    def test_get_js_tags_for_amp(self):
        context = Context()
        template = Template(
            r'{% load testimonials %}{% testimonials_js_tags is_amp=True %}'
        )
        jstag = template.render(context)
        self.assertEqual(
            jstag,
            '<script async custom-element="amp-testimonials" '
            'src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>'
        )

    def test_testimonials_tag(self):
        context = Context()
        template = Template(
            r'{% load testimonials %}{% testimonials %}'
        )
        content = template.render(context)
        self.assertEqual(
            content.replace('    ', '').replace('\n', '').replace('\t', '').strip(),
            '''
            <section class="testimonial-section" id="id_testimonials">
            <div class="container">
                <div class="mdl-grid">
                    <div class="mdl-cell mdl-cell--12-col">
                        <p class="bold-title">Pacient’s Testimonials</p>
                    </div>
                </div>
            </div>

            <div class="testimonial-slider">
                <div class="container">
                    <div class="mdl-grid">
                        <div class="mdl-cell mdl-cell--9-col mdl-cell--9-col-tablet">
                            <div class="testimonial-bg-shape">
                                <div class="swiper-container testimonial-slider-wrap swiper-container-fade
                                 swiper-container-horizontal swiper-container-wp8-horizontal">
                                    <div class="swiper-wrapper">
                                        <div class="swiper-slide swiper-slide-duplicate swiper-slide-active">
                                            <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien.
                                                 Suspendisse cursus faucibus finibus.
                                                 Curabitur ut augue finibus, luctus tortor at,
                                                 ornare erat. Nulla facilisi.
                                                 Sed est risus, laoreet et quam non, viverra accumsan leo.</p>
                                            </div>
                                            <div class="entry-footer">
                                                <figure class="user-avatar">
                                                    <img src="{}" alt="">
                                                </figure>
                                                <h3 class="testimonial-user">Russell Stephens
                                                    <span>University in UK</span>
                                                </h3>
                                            </div>
                                    </div>
                                        <div class="swiper-slide swiper-slide-duplicate swiper-slide-hide">
                                            <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                            </div>
                                            <div class="entry-footer">
                                                <figure class="user-avatar">
                                                    <img src="{}" alt="">
                                                </figure>
                                                <h3 class="testimonial-user">Roger Kohen
                                                    <span>Gagool Co</span>
                                                </h3>
                                            </div>
                                    </div>
                                        <div class="swiper-slide swiper-slide-duplicate swiper-slide-hide">
                                            <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                            </div>
                                            <div class="entry-footer">
                                                <figure class="user-avatar">
                                                    <img src="{}" alt="">
                                                </figure>
                                                <h3 class="testimonial-user">James Mccarty
                                                    <span>Big Picture Inc</span>
                                                </h3>
                                            </div>
                                    </div>
                                        <div class="swiper-slide swiper-slide-duplicate swiper-slide-hide">
                                            <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                            </div>
                                            <div class="entry-footer">
                                                <figure class="user-avatar">
                                                    <img src="{}" alt="">
                                                </figure>
                                                <h3 class="testimonial-user">Andy Cage
                                                    <span>Galaxy Zone co</span>
                                                </h3>
                                            </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="swiper-pagination-wrap">
                        <div class="container">
                            <div class="mdl-grid">
                                <div class="mdl-cell mdl-cell--9-col d-flex">
                                    <div class="swiper-pagination position-relative d-flex auto-h-margin
                                     justify-content-center align-items-center
                                     swiper-pagination-clickable swiper-pagination-bullets">
                                        <span onclick="showTestimonial('id_testimonials', 0)"
                                         class="swiper-pagination-bullet swiper-pagination-bullet-active">
                                        </span>
                                        <span onclick="showTestimonial('id_testimonials', 1)"
                                         class="swiper-pagination-bullet"></span>
                                        <span onclick="showTestimonial('id_testimonials', 2)"
                                         class="swiper-pagination-bullet"></span>
                                        <span onclick="showTestimonial('id_testimonials', 3)"
                                         class="swiper-pagination-bullet"></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''.format(
                *[t.user_avatar.url for t in self.testimonials]
            ).replace('    ', '').replace('\n', '').replace('\t', '').strip()
        )

    def test_testimonials_tag_for_tags(self):
        context = Context()
        template = Template(
            r'{% load testimonials %}{% testimonials is_amp=True %}'
        )
        content = template.render(context)
        self.assertEqual(
            content.replace('    ', '').replace('\n', '').replace('\t', '').strip(),
            '''
            <section class="testimonial-section" id="id_testimonials">
                <div class="container">
                    <div class="mdl-grid">
                        <div class="mdl-cell mdl-cell--12-col">
                            <p class="bold-title">Pacient’s Testimonials</p>
                        </div>
                    </div>
                </div>

                <div class="testimonial-slider">
                    <div class="container">
                        <div class="mdl-grid">
                            <div class="mdl-cell mdl-cell--9-col mdl-cell--9-col-tablet">
                                <div class="testimonial-bg-shape">
                                    <div class="swiper-container amp-item testimonial-slider-wrap
                                     swiper-container-fade swiper-container-horizontal
                                     swiper-container-wp8-horizontal">
                                        <div class="swiper-wrapper">
                                        <amp-carousel width="auto" controls layout="flex-item" type="slides">

                                            <div class="swiper-slide swiper-slide-duplicate swiper
                                            -slide-active">
                                                <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                                </div>
                                                <div class="entry-footer">
                                                    <figure class="user-avatar">
                                                        <amp-img src="{}"
                                                         width="24" height="24" layout="responsive" alt="">
                                                    </figure>
                                                    <h3 class="testimonial-user">Russell Stephens
                                                        <span>University in UK</span>
                                                    </h3>
                                                </div>
                                            </div>

                                            <div class="swiper-slide swiper-slide
                                            -duplicate swiper-slide-hide">
                                                <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                                </div>
                                                <div class="entry-footer">
                                                    <figure class="user-avatar">
                                                        <amp-img src="{}"
                                                         width="24" height="24" layout="responsive" alt="">
                                                    </figure>
                                                    <h3 class="testimonial-user">Roger Kohen
                                                        <span>Gagool Co</span>
                                                    </h3>
                                                </div>
                                            </div>

                                            <div class="swiper-slide swiper-slide
                                                -duplicate swiper-slide-hide">
                                                <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                                </div>
                                                <div class="entry-footer">
                                                    <figure class="user-avatar">
                                                        <amp-img src="{}"
                                                         width="24" height="24" layout="responsive" alt="">
                                                    </figure>
                                                    <h3 class="testimonial-user">James Mccarty
                                                        <span>Big Picture Inc</span>
                                                    </h3>
                                                </div>
                                            </div>

                                            <div class="swiper-slide swiper-slide
                                                -duplicate swiper-slide-hide">
                                                <div class="entry-content">
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                                 Donec malesuada lorem maximus mauris scelerisque,
                                                 at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse
                                                 cursus faucibus finibus. Curabitur ut augue finibus, luctus
                                                 tortor at, ornare erat. Nulla facilisi. Sed est risus,
                                                 laoreet et quam non, viverra accumsan leo.</p>
                                                </div>
                                                <div class="entry-footer">
                                                    <figure class="user-avatar">
                                                        <amp-img src="{}"
                                                         width="24" height="24" layout="responsive" alt="">
                                                    </figure>
                                                    <h3 class="testimonial-user">Andy Cage
                                                        <span>Galaxy Zone co</span>
                                                    </h3>
                                                </div>
                                            </div>
                                        </amp-carousel>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        '''.format(
                [t.user_avatar.url for t in self.testimonials]
            ).replace('    ', '').replace('\n', '').replace('\t', '').strip()
        )
