from .base import *
from .password import PASSWORD_PASSWORD, DB_NAME

'''
Por seguridad, recordar que hay que crear un archivo "password.py" y ahi dentro declarar la PASSWORD_PASSWORD
con el valor de la secret key de la DB, lo mismo con el nombre de la DB.
'''


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': 'postgres',
        'PASSWORD': PASSWORD_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
