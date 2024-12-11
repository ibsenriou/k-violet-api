from urllib.parse import urlparse
import environ
import io
import os
import sys
from pathlib import Path

from storages.backends.gcloud import GoogleCloudStorage
from google.oauth2 import service_account
import json
import re

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / 'src'
PUBLIC_DIR = BASE_DIR / 'public'

# Makes Django aware of the src folder and its contents for running make migrations and migrate commands
sys.path.append(os.path.join(BASE_DIR, 'src'))


SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-bi)2%bimnsvoa&+hy*fuzcoe^+@k7n-ao!&1dr@t_&f1gjm3qw'
)

APPEND_SLASH = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',


    # --- Rest Framework Installs
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django_filters',

    'corsheaders',
    'django_extensions',
    'stdimage',

    # --- Project Apps
    'src.core',
    # --- DRF Spectacular Handles API Schema Generation for OpenAPI Documentation
    'drf_spectacular',

    'test_without_migrations'


]

# Temporary middleware class
class DisableCsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        return self.get_response(request)


MIDDLEWARE = [
    'settings.settings.DisableCsrfMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # TODO - Re enable CSRF Middleware after implementing CSRF Token on Frontend
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.global_request_middleware.global_request_middleware.GlobalRequestMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


MAX_CONN_AGE = 600

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/public/staticfiles/'
STATIC_ROOT = PUBLIC_DIR / 'staticfiles'

MEDIA_ROOT = PUBLIC_DIR / 'media'
MEDIA_URL = '/public/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.CustomUser'

# Django Rest Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1000,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # Define that the API will use SessionAuthentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# Django Rest Spectacular Configuration (OpenAPI 3 Schema)
SPECTACULAR_SETTINGS = {
    'TITLE': 'K-Violet API',
    'DESCRIPTION': 'API for the K-Violet™ Application',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

# DJANGO CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# DJANGO Google Cloud SQL Configuration


# Load the settings from the environment variable
env = environ.Env()
env.read_env(io.StringIO(os.environ.get("APPLICATION_SETTINGS", None)))


DATABASE_URL = env("DATABASE_URL", default=None)
DATABASE_NAME = env("DATABASE_NAME", default=None)

if DATABASE_URL:
    if DATABASE_NAME:
        REGEX = r"postgres:\/\/[^:]*:[^@]*@\d*.\d*.\d*.\d*:\d*\/(.*)"
        OLD_DATABASE_NAME = re.search(REGEX, DATABASE_URL).group(1)
        DATABASE_URL = DATABASE_URL.replace(OLD_DATABASE_NAME, DATABASE_NAME)
    DATABASES = {"default": env.db(default=DATABASE_URL)}

# If defined, add service URL to Django security settings
CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
CLOUDRUN_WEB_SERVICE_URL = env("CLOUDRUN_WEB_SERVICE_URL", default=None)
CLOUDRUN_API_GATEWAY_URL = env("CLOUDRUN_API_GATEWAY_URL", default='http://localhost:8001')
LOCALHOST_URL = 'http://localhost:8000'

ALLOWED_HOSTS = ['*']
DEBUG = env("DEBUG", default=True)

if CLOUDRUN_SERVICE_URL:
    # Setting this value from django-environ
    SECRET_KEY = env("SECRET_KEY")

    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc, urlparse(
        CLOUDRUN_WEB_SERVICE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL, CLOUDRUN_WEB_SERVICE_URL,
                            'https://api.homespace.digital',
                            'https://app.homespace.digital'
                            ]
    CORS_ALLOWED_ORIGINS = [CLOUDRUN_SERVICE_URL, CLOUDRUN_WEB_SERVICE_URL,
                            'https://api.homespace.digital',
                            'https://app.homespace.digital'
                            ]

    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
        json.loads(env("SERVICE_ACCOUNT"))
    )


# If not defined, set DEBUG to True and ALLOWED_HOSTS to all
if not CLOUDRUN_SERVICE_URL:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

# Define static storage via django-storages[google]
SESSION_COOKIE_NAME = "__session-django"
PERSON_BUCKET = None

GS_BUCKET_NAME = env("GS_BUCKET_NAME", default=None)
GOOGLE_CLOUD_PROJECT = env("GOOGLE_CLOUD_PROJECT", default=None)
GOOGLE_CLOUD_LOCATION = env("GOOGLE_CLOUD_LOCATION", default=None)

if GS_BUCKET_NAME:
    PERSON_BUCKET = GoogleCloudStorage(
        bucket_name='homespace-digital-media-person')
    STATICFILES_DIRS = []
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    GS_DEFAULT_ACL = "publicRead"

GOOGLE_MAPS_API_KEY = env("GOOGLE_MAPS_API_KEY",
                          default="AIzaSyDnF1MYxpLDPahofqOaxKBw4rv2e_kpxHY")


DEFAULT_MAIL_SERVICE = env("DEFAULT_MAIL_SERVICE", default="mailersend")
FROM_EMAIL = env("FROM_EMAIL", default="dev-no-reply@homespace.digital")
FROM_EMAIL_NAME = env(
    "FROM_EMAIL_NAME", default="Dev - Homespace Digital")
LOCALHOST_WEBHOOK_URL = "https://webhook.site/2abeae1c-20e6-4459-938d-67c33ae5a6d4"

CLOUD_FUNCTION_ADDRESS_SEARCH = env(
    "CLOUD_FUNCTION_ADDRESS_SEARCH", default="https://southamerica-east1-homespace-digital.cloudfunctions.net/address_search")
# Optional Dj-Rest-Auth Use Http-Only Cookies
# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'django-rest-auth-test-jwt-auth'
# JWT_AUTH_REFRESH_COOKIE = 'django-rest-auth-test-my-refresh-token'

# Using for testing purposes - Django Debug Sql Queries
# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }