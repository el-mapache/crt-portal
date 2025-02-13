"""Reminder not to put secrets in this file, it is in source control """
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',  # set in docker-compose.yml
        'PORT': 5432  # default postgres port
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')
# This setting will only be used in local development
ALLOWED_HOSTS = ['localhost', '0.0.0.0']  # nosec
DEBUG = True
