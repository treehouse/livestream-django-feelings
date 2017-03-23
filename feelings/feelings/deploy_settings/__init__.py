import dj_database_url

from feelings.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.herokuapp.com',
]

INSTALLED_APPS += (
    'gunicorn',
)

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

SECRET_KEY = get_env_variable("SECRET_KEY")

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'