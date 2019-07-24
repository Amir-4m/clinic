#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .base import *  # NOQA
from django.utils.translation import ugettext_lazy as _

ROOT_URLCONF = 'clinic.urls.web'

USE_I18N = True

LANGUAGES = (
    ('en-us', _('English')),
    ('fa', _('Persian')),
)

USE_L10N = True

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    # Adds a few conveniences for perfectionists (i.e. URL rewriting)
    'django.middleware.common.CommonMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

# HTML Minify does not support django 2.0 or higher
HTML_MINIFY = get_env_var('HTML_MINIFY', str(not DEBUG)) == 'True'

TEMPLATES[0]['OPTIONS'] = {
    'debug': DEBUG,
    'context_processors': (
        'constance.context_processors.config',
        'django.template.context_processors.i18n',
        'django.template.context_processors.static',
        'django.template.context_processors.request',
        'sekizai.context_processors.sekizai',
        'clinic.context_processors.global_settings',
        'django_contrib.sites.context_processors.site_settings',
        'django_contrib.amp.context_processors.amp',
        'django.template.context_processors.media',
    ),
    # List of callables that know how to import templates from
    # various sources.
    'loaders': (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
}

INSTALLED_APPS += (
    'django.contrib.sitemaps',

    # External Apps
    'compressor',
    'sekizai',

    # Project Apps
    'django_contrib.amp',
    'django_contrib.html',
    'django_contrib.jalali',
    'django_contrib.pagination',
    'django_contrib.breadcrumb',
    'django_contrib.social',
    'django_contrib.lazy',
)

COMPRESS_ENABLED = get_env_var('COMPRESS_ENABLED', str(not DEBUG)) == 'True'

# A list of filters that will be applied to CSS.
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

IRAN_YEKAN_LICENSE = get_env_var('IRAN_YEKAN_LICENSE', '3.0')

GA_VERSION = get_env_var('GA_VERSION', 'GA1')

GA_COOKIE_NAME = get_env_var('GA_COOKIE_NAME', '_ga')
GA_COOKIE_AGE = int(get_env_var('GA_COOKIE_AGE', 2 * 365 * 24 * 60 * 60))  # 2 years
GA_COOKIE_PATH = get_env_var('GA_COOKIE_PATH', '/')
GA_COOKIE_DOMAIN = get_env_var('GA_COOKIE_DOMAIN')
GA_COOKIE_SECURE = get_env_var('GA_COOKIE_SECURE', 'False') == 'True'

GTM_AMP_CONF_URL = get_env_var('GTM_AMP_CONF_URL', 'https://www.googletagmanager.com/amp.json')
GTM_CONFIG_CACHE_TIMEOUT = int(get_env_var('GTM_CONFIG_CACHE_TIMEOUT', 10 * 60))  # 10 minutes

AMP_CONFIG_CORS_ORIGIN_WHITELIST = [i for i in get_env_var('AMP_CONFIG_CORS_ORIGIN_WHITELIST', "").split(",") if i]
