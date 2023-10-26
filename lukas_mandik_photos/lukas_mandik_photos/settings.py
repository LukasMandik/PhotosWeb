"""
Django settings for lukas_mandik_photos project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
# after import os
from oscar.defaults import *
from pathlib import Path

import environ

env = environ.Env()

environ.Env.read_env()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "lvh.me"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


LOGIN_REDIRECT_URL = '/'

LIKED_PHOTOS_COOKIE_MAX_AGE = 31536000

USE_TZ = True

INSTALLED_APPS = [
    'livereload',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_countries',

    'photos_web',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'oscar',
    'oscar.apps.analytics',
    # 'apps.checkout.apps',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue',
    # 'lukas_mandik_photos.catalogue.apps.CatalogueConfig',
    # 'oscar.apps.checkout',
    'apps.checkout.apps.CheckoutConfig',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.partner',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'oscar.apps.order',
    'oscar.apps.customer',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'oscar.apps.communication',
    'oscar.apps.dashboard',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.catalogue',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.shipping',
    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]

SITE_ID = 2

SOCIALACCOUNT_LOGIN_ON_GET = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'lukas_mandik_photos.urls'
#
#
# MIDDLEWARE_CLASSES = (
#     'livereload.middleware.LiveReloadScript',
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
                # oscars context processors
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',

]
WSGI_APPLICATION = 'lukas_mandik_photos.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': env('DB_NAME'),
        # 'USER': env('DB_USERNAME'),
        # 'PASSWORD': env('DB_PASSWORD'),
        # 'HOST': env('DB_HOST'),
        # 'PORT': env('DB_PORT'),
    }
}
import dj_database_url

DATABASES["default"] = dj_database_url.parse(env('EXTERNAL_DB'))


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# STATIC_URL = '/static/'
# MEDIA_URL = '/images/'
#
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]
#
# MEDIA_ROOT = BASE_DIR / 'static/images'
# STATIC_ROOT = BASE_DIR / 'staticfiles'







# run python3 manage.py collectstatic
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


MEDIA_URL = '/images/'


# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]

MEDIA_ROOT = BASE_DIR / 'static/images'
# STATIC_ROOT = BASE_DIR / 'staticfiles'





# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

EXIFTOOL_PATH = '/usr/local/bin/exiftool'  # cesta k exiftoolu na vašom počítači

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Pre Django Allauth

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access type': "online"
        }
    }
}
LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'  # Zmeňte toto na URL, na ktorú chcete presmerovať používateľov po prihlásení
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Nastavte toto na 'none', ak nechcete overenie e-mailu

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name()
# ACCOUNT_ADAPTER = 'lukas_mandik_photos.allauth_adapter.CustomAccountAdapter'


ACCOUNT_FORMS = {
    'signup': 'photos_web.forms.MyCustomSignupForm',
}

# ACCOUNT_SIGNUP_FORM_CLASS = 'photos_web.forms.CustomSignupForm'


# OSCAR_REQUIRED_ADDRESS_FIELDS = (
#     'first_name', 'last_name', 'line1', 'line4', 'postcode', 'country'
# )
# OSCAR_DYNAMIC_CLASS_LOADER = 'oscar.core.loading.default_class_loader'
# OSCAR_DEFAULT_CURRENCY = 'USD'
# OSCAR_SLUG_FUNCTION = 'oscar.core.utils.default_slugifier'
# OSCAR_SLUG_MAP = ()
# OSCAR_SLUG_BLACKLIST = ()
# OSCAR_SLUG_ALLOW_UNICODE = True
# OSCAR_ALLOW_ANON_CHECKOUT = False
# OSCAR_EAGER_ALERTS = False
# OSCAR_DELETE_IMAGE_FILES = True
# OSCAR_PRODUCTS_PER_PAGE = 10  # Alebo akúkoľvek inú hodnotu, ktorú chcete nastaviť
# OSCAR_OFFERS_PER_PAGE = 20  # Alebo akúkoľvek inú hodnotu, ktorú chcete nastaviť
# OSCAR_REVIEWS_PER_PAGE = 10  # Alebo akúkoľvek inú hodnotu, ktorú chcete nastaviť
# OSCAR_RECENTLY_VIEWED_COOKIE_NAME = 'recently_viewed_products'  # Alebo akýkoľvek iný názov cookie, ktorý chcete použiť
# OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME = 1209600
# OSCAR_RECENTLY_VIEWED_COOKIE_SECURE = False  # Alebo True, ak chcete, aby sa cookie odosielali iba cez HTTPS
# OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
# OSCAR_SEARCH_FACETS = {
#     'fields': {
#         # ...
#     },
#     'queries': {},
# }
# OSCAR_SLUG_MAP = {}  # prípadne prispôsobte hodnoty podľa potreby
# OSCAR_SLUG_BLACKLIST = {}  # prípadne prispôsobte hodnoty podľa potreby
OSCAR_SEND_REGISTRATION_EMAIL = True

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
COUNTRY_CODE = 'SK'
CURRENCY_CODE = 'EUR'

COUNTRIES_FIRST = True

STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')

STRIPE_CURRENCY = "EUR"

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # port pre SMTP server
EMAIL_USE_TLS = True  # pre šifrované spojenie
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'swipe47@gmail.com'
EMAIL_HOST_PASSWORD = ''
