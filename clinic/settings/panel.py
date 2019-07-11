#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .base import *  # NOQA

ROOT_URLCONF = 'clinic.urls.panel'

USE_I18N = False

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

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-X_FRAME_OPTIONS
X_FRAME_OPTIONS = 'DENY'

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    # Enables session support.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    # Adds a few conveniences for perfectionists (i.e. URL rewriting)
    'django.middleware.common.CommonMiddleware',
    # Adds protection against Cross Site Request Forgeries
    'django.middleware.csrf.CsrfViewMiddleware',
    # Adds the user attribute, representing the currently-logged-in user
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Enables cookie- and session-based message support.
    'django.contrib.messages.middleware.MessageMiddleware',
    # Simple clickjacking protection via the X-Frame-Options header.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

INSTALLED_APPS += (
    # Internal Django Apps
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',

    # External Apps
    'ckeditor',
    'ckeditor_uploader',
    'colorfield',
    'captcha',

    # Project Apps
    'django_contrib.recaptcha',
)

if DEBUG or TEST:
    RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
    RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

else:  # pragma: no cover
    RECAPTCHA_PUBLIC_KEY = get_env_var('RECAPTCHA_PUBLIC_KEY', '')
    RECAPTCHA_PRIVATE_KEY = get_env_var('RECAPTCHA_PRIVATE_KEY', '')
