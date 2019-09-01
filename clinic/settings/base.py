#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from kombu import Exchange, Queue


def get_env_var(key, default=None):
    return os.environ.get('CLINIC_%s' % key, default)


# Celery settings
# http://docs.celeryproject.org/en/latest/configuration.html
# https://denibertovic.com/posts/celery-best-practices/
# http://celery.readthedocs.org/en/latest/userguide/monitoring.html

# Broker settings
BROKER_URL = get_env_var('BROKER_URL', 'amqp://guest:guest@localhost//')

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ALWAYS_EAGER = get_env_var('CELERY_ALWAYS_EAGER', 'False') == 'True'

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'default'

# http://docs.celeryproject.org/en/latest/configuration.html#celery-queues
CELERY_QUEUES = (
    Queue('default', Exchange('clinic', type='direct'), routing_key='default'),
)

CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

# http://docs.celeryproject.org/en/latest/configuration.html#celery-routes
# CELERY_ROUTES = {}

# Whether to store the task return values or not.
CELERY_IGNORE_RESULT = True

# If you still want to store errors, just not successful return values
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False

# The backend used to store task results.
# CELERY_RESULT_BACKEND = ''

# Time (in seconds, or a timedelta object) for when after stored task
# tombstones will be deleted.
# CELERY_TASK_RESULT_EXPIRES = 0

# Django settings for Clinic project.

# The top directory for this project. Contains requirements/, manage.py,
# and README.rst, a clinic directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'clinic')

DEBUG = get_env_var('DEBUG', 'False') == 'True'

TEST = get_env_var('TEST', 'False') == 'True'

ADMINS = (
    ('Saeed Salehian', 'saeed@upkook.com'),
    ('Mohsen Javidpanah', 'moshen212@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS', "127.0.0.1,localhost").split(",")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_var('DEFAULT_DATABASE_NAME', 'fake-db'),
        'USER': get_env_var('DEFAULT_DATABASE_USER', 'postgres'),
        'PASSWORD': get_env_var('DEFAULT_DATABASE_PASSWORD', ''),
        'HOST': get_env_var('DEFAULT_DATABASE_HOST', '127.0.0.1'),
        'PORT': get_env_var('DEFAULT_DATABASE_PORT', '5432'),
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_var('SECRET_KEY', 'fake-key')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = get_env_var('TIME_ZONE', 'Asia/Tehran')

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = get_env_var('LANGUAGE_CODE', 'en-us')

SITE_ID = get_env_var('SITE_ID', 1)

SITE_URL = get_env_var('SITE_URL', 'http://127.0.0.1/')

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = get_env_var('MEDIA_ROOT', os.path.join(PROJECT_ROOT, 'public', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = get_env_var('MEDIA_URL', '/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = get_env_var('STATIC_ROOT', os.path.join(PROJECT_ROOT, 'public', 'static'))

# Path to generated static files from JavaScript catalog
STATICI18N_ROOT = os.path.join(PROJECT_PATH, 'static', )

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = get_env_var('STATIC_URL', '/static/')

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'DIRS': (
            os.path.join(PROJECT_PATH, 'templates'),
        ),
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': (
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django_contrib.amp.context_processors.amp',
            ),
            # List of callables that know how to import templates from
            # various sources.
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )
        }
    }
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {'user_attributes': ('email', 'username')}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# List of compiled regular expression objects representing User-Agent strings
# that are not allowed to visit any page, system-wide.
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-DISALLOWED_USER_AGENTS
DISALLOWED_USER_AGENTS = []

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-APPEND_SLASH
APPEND_SLASH = get_env_var('APPEND_SLASH', 'True') == 'True'

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-PREPEND_WWW
PREPEND_WWW = get_env_var('PREPEND_WWW', 'False') == 'True'

# A boolean that specifies whether to output the ETag header.
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_ETAGS
USE_ETAGS = True

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    # Adds a few conveniences for perfectionists (i.e. URL rewriting)
    'django.middleware.common.CommonMiddleware',
)

# Security Settings
SECURE_BROWSER_XSS_FILTER = get_env_var('SECURE_BROWSER_XSS_FILTER', 'True') == 'True'
SECURE_CONTENT_TYPE_NOSNIFF = get_env_var('SECURE_CONTENT_TYPE_NOSNIFF', 'True') == 'True'
SECURE_HSTS_INCLUDE_SUBDOMAINS = get_env_var('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'False') == 'True'
SECURE_HSTS_SECONDS = get_env_var('SECURE_HSTS_SECONDS', 0)
SECURE_HSTS_PRELOAD = get_env_var('SECURE_HSTS_PRELOAD', 'False') == 'True'
SECURE_SSL_REDIRECT = get_env_var('SECURE_SSL_REDIRECT', 'False') == 'True'
SECURE_SSL_HOST = get_env_var('SECURE_SSL_HOST')
SECURE_REDIRECT_EXEMPT = get_env_var('SECURE_REDIRECT_EXEMPT', '').split(',')

if DEBUG or TEST:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'sessions': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

else:  # pragma: no cover
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

LOGIN_URL = get_env_var('LOGIN_URL', '/login')

ROOT_URLCONF = 'clinic.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'clinic.wsgi.application'

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(PROJECT_PATH, 'logs', 'clinic.log'),
            'maxBytes': 20 * 1024 * 1024,  # 20 MBs
            'backupCount': 40,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'] if DEBUG else ['file'],
            'propagate': True,
            'level': 'WARNING' if DEBUG else 'ERROR',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING' if DEBUG else 'ERROR',
            'propagate': True,
        },
        'clinic': {
            'handlers': ['console'] if DEBUG else ['file'],
            'level': 'DEBUG' if DEBUG else 'ERROR',
            'propagate': True,
        },
    }
}

INSTALLED_APPS = (
    # Internal Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Include app here if you use custom User
    'django_contrib.auth',

    # External Apps
    # To Persist Dynamic Settings
    'constance.backends.database',
    'ckeditor',
    'ckeditor_uploader',

    # To configure Celery tasks from admin panel
    'django_celery_beat',
    'django_cleanup',

    'django_contrib.sites',
    'django_contrib.seo',

    # Widget Apps
    'clinic.apps.carousel',
    'clinic.apps.departmentsbox',
    'clinic.apps.testimonials',

    # Page Apps
    'clinic.apps.home',
    'clinic.apps.about_us',
    'clinic.apps.contact',
    'clinic.apps.services',
)

if DEBUG:  # pragma: no cover
    INSTALLED_APPS += ('django_extensions',)

UPLOAD_PATH = get_env_var('UPLOAD_PATH', os.apth.join(MEDIA_ROOT, 'ups/'))

CKEDITOR_UPLOAD_PATH = get_env_var('CKEDITOR_UPLOAD_PATH', os.apth.join(MEDIA_ROOT, 'ck_ups/'))
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    'basic': {
        'toolbar': 'Basic',
        'toolbar_Basic': [
            ['Source'], ['Bold', 'Italic'], ['Link', 'Unlink']
        ]
    },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            [
                'Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike',
                'SpellChecker', 'Undo', 'Redo'
            ],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
    },
    'amp': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            [
                'Format', 'Bold', 'Italic', 'Underline', 'Strike',
                'SpellChecker', 'Undo', 'Redo'
            ],
            ['Link', 'Unlink', 'Anchor'], ['Blockquote', 'Image', 'HorizontalRule'], ['Source'],
        ],
        'extraAllowedContent': [
            'amp-social-share', 'amp-social-share[type]', 'amp-social-share[role]',
            'amp-social-share[height]', 'amp-social-share[width]',
            'amp-social-share[data-param-text]', '*(ck-*)', '*(mdl-button-*)'
        ],
    },
}

# Set model for using in authentication
AUTH_USER_MODEL = 'django_auth.User'

# cookie and session domain name. must be string
SESSION_COOKIE_DOMAIN = get_env_var('SESSION_COOKIE_DOMAIN')

CSRF_COOKIE_DOMAIN = get_env_var('CSRF_COOKIE_DOMAIN')

# Controls where Django stores session data.
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = get_env_var('SESSION_CACHE_ALIAS', 'default')
# redis://[:password@]host[:port][/db-number][?option=value]
# unix://[:password]@/path/to/socket.sock[?option=value]
SESSION_REDIS = {'url': get_env_var('SESSION_REDIS_URL', 'redis://localhost:6379/1')}

# The age of session cookies, in seconds.
SESSION_COOKIE_AGE = 2 * 7 * 24 * 60 * 60  # 2 weeks

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Subject-line prefix for email messages sent.
EMAIL_SUBJECT_PREFIX = get_env_var('EMAIL_SUBJECT_PREFIX', '[Clinic] ')

DEFAULT_FROM_EMAIL = get_env_var('DEFAULT_FROM_EMAIL', 'Clinic <noreply@surenavision.com>')

SERVER_EMAIL = get_env_var('SERVER_EMAIL', 'Surena Vision <noreply@surenavision.com>')

# The host to use for sending email.
EMAIL_HOST = get_env_var('EMAIL_HOST', 'localhost')

# Username to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_USER = get_env_var('EMAIL_HOST_USER', '')

# Password to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_PASSWORD = get_env_var('EMAIL_HOST_PASSWORD', '')

# Port to use for the SMTP server defined in EMAIL_HOST.
EMAIL_PORT = get_env_var('EMAIL_PORT', 587)

# Whether to use a TLS (secure) connection when talking to the SMTP server.
EMAIL_USE_TLS = get_env_var('EMAIL_USE_TLS', 'True') == 'True'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}
CONSTANCE_CONFIG = {
    'NAME': ('MedArt', 'Clinic Name'),
    'LOGO': ('logo.png', 'Clinic Logo', 'image_field'),
    'PHONE': ('+345867788892', 'Enter Clinic Phone Number'),
    'EMERGENCY_PHONE': ('+345867788892', 'Enter Clinic Emergency Phone Number'),
    'EMERGENCY_TEXT': (
        'Lorem ipsum dolor sit amet, cons ectetur adipiscing elit. '
        'Donec males uada lorem maximus mauris sceler isque, at rutrum nulla.',

        'Enter Clinic Emergency Box Text'
    ),
    'EMAIL': ('yourmail@gmail.com', 'Enter Clinic Email'),
    'ADDRESS': ('Mitlton Str. 26-27 London UK', 'Enter Clinic Address'),
    'MONDAY_WORKING_TIME': ('9:30 - 15:30', 'If be empty not show'),
    'TUESDAY_WORKING_TIME': ('', 'If be empty not show'),
    'WENDSDAY_WORKING_TIME': ('', 'If be empty not show'),
    'Thursday_WORKING_TIME': ('9:30 - 15:30', 'If be empty not show'),
    'FRIDAY_WORKING_TIME': ('8:00 - 18:30', 'If be empty not show'),
    'SATURDAY_WORKING_TIME': ('9:30 - 17:30', 'If be empty not show'),
    'SUNDAY_WORKING_TIME': ('9:30 - 15:00', 'If be empty not show'),
    'COPYRIGHT': (
        '''<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien.
           </p>
           <p class="copyright">
               Copyright © 2019 All rights reserved | This template is made with
               <i class="fa fa-heart" aria-hidden="true"></i>
               by
               <a href="https://colorlib.com/" target="_blank"> Colorlib</a>
           </p>'''.replace('  ', ''),

        'Enter the copyright text'
    ),
    'MAP': (
        r'https://maps.google.com/maps?q=university of san francisco&t=&z=15&ie=UTF8&iwloc=&output=embed',
        'Map full address'
    )
}
