from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
STATICFILES_DIRS = [BASE_DIR / "project" / "static",]
MEDIA_ROOT = BASE_DIR / "project" / "media"