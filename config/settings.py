import os
import dj_database_url
from urllib.parse import quote
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = 'django-insecure-portfolio-key-at-least-50-chars-long'
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    "portfolio",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Prioritize building from separate variables to avoid URL parsing issues with special characters
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT', '6543')
db_name = os.environ.get('DB_NAME')

import sys

# Diagnostic logging (will show in Vercel logs)
print(f"--- DB ENV CHECK START ---", flush=True)
print(f"DB_USER: {db_user}", flush=True)
print(f"DB_HOST: {db_host}", flush=True)
print(f"DB_PORT: {db_port}", flush=True)
print(f"DB_NAME: {db_name}", flush=True)
print(f"DATABASE_URL present: {bool(os.environ.get('DATABASE_URL'))}", flush=True)

# --- DIRECT DICT DB CONFIG (Safest for special characters) ---
if all([db_user, db_password, db_host, db_port, db_name]):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': db_user,
            'PASSWORD': db_password,
            'HOST': db_host,
            'PORT': db_port,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }
    print("STATUS: Configured via DIRECT DICT (No ParseError risk)", flush=True)
elif os.environ.get('DATABASE_URL'):
    conf = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES = {'default': conf}
    print("STATUS: Configured from DATABASE_URL", flush=True)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print("STATUS: Configured from SQLITE (Fallback)", flush=True)

# FINAL OVERRIDE: Ensure NAME is never empty for postgres
for db_key in DATABASES:
    config = DATABASES[db_key]
    if config.get('ENGINE') and 'postgresql' in config.get('ENGINE'):
        if not config.get('NAME'):
            config['NAME'] = 'postgres'
            print(f"FORCED NAME='postgres' for {db_key}", flush=True)

print(f"--- DB FINAL STATE ---", flush=True)
print(f"ENGINE: {DATABASES['default'].get('ENGINE')}", flush=True)
print(f"NAME: {DATABASES['default'].get('NAME')}", flush=True)
print(f"--- DB ENV CHECK END ---", flush=True)
sys.stdout.flush()

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

UNFOLD = {
    "SITE_TITLE": "Portfolio Admin",
    "SITE_HEADER": "Modern Portfolio",
    "SITE_URL": "/",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
    },
    "COLORS": {
        "primary": {
            "50": "239 246 255",
            "100": "219 234 254",
            "200": "191 219 254",
            "300": "147 197 253",
            "400": "96 165 250",
            "500": "59 130 246",
            "600": "37 99 235",
            "700": "29 78 216",
            "800": "30 64 175",
            "900": "30 58 138",
            "950": "23 37 84",
        },
    },
}
