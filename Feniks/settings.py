# -*- coding: utf-8 -*-
import os
import socket
from secret import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = secret_key

ENABLE_SSL = False

LOGIN_REDIRECT_URL = '/'

# AUTH_PROFILE_MODULE = 'accounts.userprofile'

AUTH_USER_MODEL = 'accounts.UserProfile'

if socket.gethostname() == 'asus-UX32LN':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]

SITE_ID = 1

PRODUCTS_PER_PAGE = 40

PRODUCTS_PER_ROW = 4

SESSION_AGE_DAYS = 7
SESSION_COOKIE_AGE = 60 * 60 * 24 * SESSION_AGE_DAYS

# # EMAIL
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = email_host_user
# EMAIL_HOST_PASSWORD = email_host_password
# EMAIL_PORT = 587

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = email_host_user
SERVER_EMAIL = 'django@my-domain.com'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'catalog',
    'search',
    'stats',
    'accounts',
    'cart',
    'bootstrapform',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Feniks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'myutils.context_processors.ecomstore',
            ],
        },
    },
]

WSGI_APPLICATION = 'Feniks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'feniks',
        'USER': pg_username,
        'PASSWORD': pg_password,
        'HOST': 'localhost',
        'PORT': '',
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

# USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

if socket.gethostname() != 'asus-UX32LN':
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

SITE_NAME = u'Феникс'
META_KEYWORDS = u'мебель, мягкая мебель, офисная мебель, купить мебель, диваны, кресла, прохладный, кабардино-балкария'
META_DESCRIPTION = u'Мебельный Салон Феникс'

ADMINS = [('feniks', 'feniks-kbr@yandex.ru'),('lse', 'lse1983@mail.ru')]
