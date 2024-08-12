import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = os.environ['WEBSITE_HOSTNAME']
CSRF_TRUSTED_ORIGINS = ['HTTPS://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')