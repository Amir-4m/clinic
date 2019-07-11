#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from .base import *  # NOQA

TEMPLATES[0]['OPTIONS'] = {
    'debug': DEBUG,
    'context_processors': (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.template.context_processors.request',
        'django.template.context_processors.i18n',
        'django.template.context_processors.static',
        'django.template.context_processors.csrf',
    ),
    # List of callables that know how to import templates from
    # various sources.
    'loaders': (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
}

MIDDLEWARE = (
    # Enables session support.
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Adds protection against Cross Site Request Forgeries
    'django.middleware.csrf.CsrfViewMiddleware',
    # Adds the user attribute, representing the currently-logged-in user
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Enables cookie- and session-based message support.
    'django.contrib.messages.middleware.MessageMiddleware',

)

INSTALLED_APPS += (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    # External Apps
    'ckeditor',
    'ckeditor_uploader',
    'colorfield',
    'compressor',
    'sekizai',

    'django_contrib.amp',
    'django_contrib.html',
    'django_contrib.jalali',
    'django_contrib.social',

    # Project Apps
)
