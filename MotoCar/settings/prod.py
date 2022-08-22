from .base import *
import django_on_heroku
# django_on_heroku.settings(locals())
from decouple import config


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['127.0.0.1','.localhost']
ALLOWED_HOSTS = [
    'motocar-carsell.herokuapp.com'
]