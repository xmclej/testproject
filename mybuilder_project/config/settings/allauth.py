# Settings file for the Django-allauth package
import os
from config.settings.base import INSTALLED_APPS

# print('settings-allauth')
INSTALLED_APPS += [
    # 'django.contrib.auth',      # already in base.py
    # 'django.contrib.messages',  # already in base.py
    # 'django.contrib.sites',     # already in base.py
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# Added for django-allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1     # Required for django-allauth
# See https://django-allauth.readthedocs.io/en/latest/configuration.html for options

ACCOUNT_EMAIL_REQUIRED = True               # required based on ACCOUNT_AUTHENTICATION_METHOD
ACCOUNT_AUTHENTICATION_METHOD = "username_email"     # specifies the login method i.e. username or email in this case
ACCOUNT_UNIQUE_EMAIL = True                 # enforce uniqueness of email addresses

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = "mandatory"    # requires email verification to occur

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 15       # prevent brute forcing
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300    # prevent brute forcing
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True  # include later after testing
# ACCOUNT_USERNAME_BLACKLIST =[]
LOGIN_REDIRECT_URL = '/'    # changes default from /accounts/profile to ...

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '1056366403669-5bgsd7ug0o0b2ascj3lk1t39dha5ab2a.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}
# Settings for django-allauth and sendgrid.com
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
# EMAIL_MAIN = 'jason.mcleod@outlook.co.nz'
DEFAULT_FROM_EMAIL = "jason.mcleod@outlook.co.nz"   # required for sendgrid.com
