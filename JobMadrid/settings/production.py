from .base import *
from .password import PASSWORD_PASSWORD


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'JobMadrid',
        'USER': 'postgres',
        'PASSWORD': PASSWORD_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
