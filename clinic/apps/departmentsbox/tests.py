#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from unittest import skipIf

from bs4 import BeautifulSoup
from django.test import TestCase
from django.template import Context, Template
from django.utils.safestring import mark_safe

from .apps import DepartmentsboxConfig
from .services import DepartmentService


@skipIf(
    os.environ.get('DJANGO_SETTINGS_MODULE') != 'clinic.settings.web',
    'This tests only run if ssettings module set as "clinic.settings.web"'
)
class DepartmentsBoxTestCase(TestCase):
    def setUp(self):
        self.departments = DepartmentService.get_all_departments()

    def test_departmentsbox_appconfig(self):
        self.assertEqual(DepartmentsboxConfig.name, 'departmentsbox')

    def test_department_model_to_string_value(self):
        self.assertEqual(self.departments[0].title, str(self.departments[0]))

    def test_department_model_preview(self):
        self.assertEqual(
            self.departments[0].preview,
            mark_safe('<img src="{}">'.format(self.departments[0].logo.url))
        )

    def test_get_departmentsbox_css_tags(self):
        context = Context()
        temp = Template(r'{% load departmentsbox %}{% departmentsbox_css_tags %}')
        csstags = temp.render(context)
        self.assertEqual(
            csstags,
            '<link rel="stylesheet" href="/static/departmentsbox/css/departmentsbox.css">'
        )

        context = Context({'bg_image': 'x/y/z.png'})
        temp = Template(r'{% load departmentsbox %}{% departmentsbox_css_tags bg_image=bg_image %}')
        csstags = temp.render(context)
        self.assertEqual(
            csstags.strip(),
            '''
        <link rel="stylesheet" href="/static/departmentsbox/css/departmentsbox.css">
        <style>
        .our-departments {
            background: url(x/y/z.png) no-repeat;
            background-size: cover;
        }
        </style>'''.strip()
        )

    def test_get_departmentsbox_css_tags_for_amp(self):
        context = Context()
        temp = Template(r'{% load departmentsbox %}{% departmentsbox_css_tags is_amp=True %}')
        csstags = temp.render(context)
        self.assertEqual(
            csstags,
            '<link rel="stylesheet" href="/static/departmentsbox/css/departmentsbox.css">'
        )

        context = Context({'bg_image': 'x/y/z.png'})
        temp = Template(
            r'{% load departmentsbox %}{% departmentsbox_css_tags is_amp=True bg_image=bg_image %}'
        )
        csstags = temp.render(context)
        self.assertEqual(
            csstags.strip(),
            '''
        <link rel="stylesheet" href="/static/departmentsbox/css/departmentsbox.css">
        <style>
        .our-departments {
            background: url(x/y/z.png) no-repeat;
            background-size: cover;
        }
        </style>'''.strip()
        )

    def test_depatrmentsbox_tag(self):
        context = Context({'bg_image': 'x/y/z.png'})
        temp = Template(r'{% load departmentsbox %}{% departmentsbox %}')
        tagcontent = temp.render(context)
        self.assertEqual(
            BeautifulSoup(tagcontent).text.replace('\n', '').replace('\t', '').replace(' ', ''),
            BeautifulSoup(
                '''
                <div class="our-departments"><div class="container"><div class="mdl-grid">
                <div class="mdl-cell mdl-cell--12-col"><div class="our-departments-wrap">
                <h2>Our Departments</h2>
                <div class="mdl-grid">
                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Cardioology</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Donec malesuada lorem maximus mauris.</p>
                        </div>
                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Gastroenterology</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Medical Lab</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Dental Care</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Surgery</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Neurology</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Orthopaedy</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Pediatry</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>

                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                    <div class="our-departments-cont">
                        <header class="entry-header d-flex flex-wrap align-items-center">
                            <img src="{}" alt="">
                            <h3>Ophthalmology</h3>
                        </header>
                        <div class="entry-content">
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                             Donec malesuada lorem maximus mauris.</p>
                        </div>

                    </div>
                </div>
                </div></div></div></div></div></div>'''.format(*[dep.logo.url for dep in self.departments])
            ).text.replace('\n', '').replace('\t', '').replace(' ', '')
        )

    def test_depatrmentsbox_tag_for_amp(self):
        context = Context({'bg_image': 'x/y/z.png'})
        temp = Template(r'{% load departmentsbox %}{% departmentsbox is_amp=True %}')
        tagcontent = temp.render(context)
        # import pdb; pdb.set_trace()
        self.assertEqual(
            BeautifulSoup(tagcontent).text.replace('\n', '').replace('\t', '').replace(' ', ''),
            BeautifulSoup(
                '''
                <div class="our-departments amp-item"><div class="container"><div class="mdl-grid">
                    <div class="mdl-cell mdl-cell--12-col">
                        <div class="our-departments-wrap">
                            <h2>Our Departments</h2>
                            <div class="mdl-grid">

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex
                                         flex-wrap align-items-center amp-item">
                                            <amp-img src="{}"
                                             width="36" height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Cardioology</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-center amp-item">
                                            <amp-img src="{}" width="36"
                                             height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Gastroenterology</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-center amp-item">
                                            <amp-img src="{}" width="36"
                                             height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Medical Lab</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex
                                         flex-wrap align-items-center amp-item">
                                            <amp-img src="{}" width="36"
                                             height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Dental Care</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop
                                 mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-center amp-item">
                                            <amp-img src="{}"
                                             width="36" height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Surgery</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-center amp-item">
                                            <amp-img src="{}" width="36"
                                             height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Neurology</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop
                                 mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-center amp-item">
                                            <amp-img src="{}"
                                             width="36" height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Orthopaedy</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col mdl-cell--4-col-desktop
                                 mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex flex-wrap
                                         align-items-centeramp-item">
                                            <amp-img src="{}"
                                             width="36" height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Pediatry</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="mdl-cell mdl-cell--12-col
                                 mdl-cell--4-col-desktop mdl-cell--6-col-tablet">
                                    <div class="our-departments-cont">
                                        <header class="entry-header d-flex
                                         flex-wrap align-items-center amp-item">
                                            <amp-img src="{}"
                                            width="36" height="36" layout="fixed" alt=""></amp-img>
                                            <h3>Ophthalmology</h3>
                                        </header>
                                        <div class="entry-content">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                             Donec malesuada lorem maximus mauris.</p>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div></div></div></div>'''.format(*[dep.logo.url for dep in self.departments])
            ).text.replace('\n', '').replace('\t', '').replace(' ', '')
        )
