from .base import * 
import dj_database_url
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
SECRET_KEY = config("SECRET_KEY")

DATABASES= {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'rpgquiz/static')]
STATICFILES_LOCATION = 'static'
STATIC_URL = '/static/'