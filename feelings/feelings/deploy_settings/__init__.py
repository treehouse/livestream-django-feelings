import dj_database_url

from feelings.settings import *

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} env variable".format(var_name)
        if DEBUG:
            warnings.war(error_msg)
        else:
            raise ImproperlyConfigured(error_msg)


DEBUG = False
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

INSTALLED_APPS += (
    'gunicorn',
)

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECRET_KEY = get_env_variable("SECRET_KEY")

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'