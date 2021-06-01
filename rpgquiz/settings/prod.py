from .base import * 
import dj_database_url
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
SECRET_KEY = config("SECRET_KEY")

DATABASES= {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }