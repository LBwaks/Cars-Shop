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


django_on_heroku.settings(locals(),staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']

DEBUG_PROPAGATE_EXCEPTIONS =True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'datefmt':"%d/%b/%Y %H:%M:%S",
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUD',            
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
       
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level':'DEBUG',
            'propagate': True,

        },
               
    }
}