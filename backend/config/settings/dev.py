# config/settings/dev.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# This ensures Django knows where to store the database file relative to the root
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}