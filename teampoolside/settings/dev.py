# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mf#8zllbn8bejrs&0utv$+u&h47*6v&r7dm*%&0^bv^e_fk(e6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teampoolside',
        'USER': 'lucha',
        'PASSWORD': 'lucha',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MEDIA_ROOT = '~/teampoolsi.de/media/'
MEDIA_URL = '/media/'