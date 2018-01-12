"""
Django settings for shopstar project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4w)-iwy5!wu*f+9zl*iv0l(o4bhh#pkcte7*njfyl1-$7tt)s8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['havannashop.herokuapp.com','shopstar.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerce.apps.EcommerceConfig',
    'rest_framework',
    'rest_framework.authtoken'

    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopstar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopstar.wsgi.application'




#REST_FRAMEWORK = {
   # 'EXCEPTION_HANDLER': 'ecommerce.exceptions.core_exception_handler',
   # 'NON_FIELD_ERRORS_KEY': 'error',
   # 'DEFAULT_AUTHENTICATION_CLASSES': (
   #     'rest_framework.authentication.TokenAuthentication',
  #      'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
  #  ),
  #  'DEFAULT_PERMISSION_CLASSES': (
  #      'rest_framework.permissions.IsAdminUser',
  #  ),
#}


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Shopstar',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
        {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Shopstar',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '/Applications/MAMP/tmp/mysql.sock',
        'PORT': '',
    }
}

AUTH_USER_MODEL = 'ecommerce.User'

REST_FRAMEWORK = {


    'DEFAULT_AUTHENTICATION_CLASSES': (
        'ecommerce.backend.backends.JWTAuthentication',
   ),
}

#AUTHENTICATION_BACKENDS = ('ecommerce.backends.JWTAuthentication','django.contrib.auth.backends.ModelBackend',)
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

SECURE_SSL_REDIRECT = False

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')