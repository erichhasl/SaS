"""
Django settings for sas_web project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

deployed = '1' == os.environ.get('DJANGO_DEPLOY', '0')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',
                            'dnwe1fairy&@7=qoe7(w0bahnt9(&%zn8bph5&-r$1*s2$d2@h')

# SECURITY WARNING: don't run with debug turned on in production!
debug = os.environ.get('DJANGO_DEBUG', None)
if debug:
    DEBUG = False if debug == '0' else True
else:
    DEBUG = True

allowed = os.environ.get('DJANGO_ALLOWED_HOST', None)
if allowed is not None:
    ALLOWED_HOSTS = allowed.split(",")
else:
    ALLOWED_HOSTS = []

# Define media paths e.g. for image storage
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT',
os.path.join((os.path.join(BASE_DIR, os.pardir)), "media"))

# x forward
USE_X_FORWARDED_HOST = True

# Application definition

INSTALLED_APPS = (
    'captcha',
    'datenbank',
    'meingoethopia',
    'startpage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'sas_web.block_ip.BlockedIpMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sas_web.urls'

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
                'sas_web.contexts.appname',
            ],
        },
    },
]

WSGI_APPLICATION = 'sas_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'sas_db'),
        'OPTIONS': {
            'read_default_file': os.environ.get('DJANGO_DATABASE_CONFIG',
                                                os.path.join(BASE_DIR, 'my.cnf'))
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT',
                             os.path.join((os.path.join(BASE_DIR, os.pardir)), "static"))

# Email setup

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = 587 if deployed else 25
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True if deployed else False

EMAIL_ARBEITSMINISTERIUM = os.environ.get('EMAIL_ARBEITSMINISTERIUM', '')
EMAIL_ARBEITSMINISTERIUM_USER = os.environ.get('EMAIL_ARBEITSMINISTERIUM', '')
EMAIL_ARBEITSMINISTERIUM_PASSWORD = os.environ.get('EMAIL_ARBEITSMINISTERIUM_PASSWORD', '')
