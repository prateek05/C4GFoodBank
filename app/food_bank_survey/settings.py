"""
Django settings for food_bank_survey project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
QR_CODE_STORAGE_LOCATION = os.environ.get(
    "QR_CODE_STORAGE_LOCATION", default=f"{BASE_DIR}/qr_codes"
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    default="django-insecure-^8ocy$+4b@(v(=sx9ch79!8o3*m(4h%z0$y&73%*x7!@4!c_q+",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    default="0.0.0.0,127.0.0.1,localhost,ec2-3-91-49-197.compute-1.amazonaws.com,c4gfoodbank.azurewebsites.net",
).split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    "campaigns.apps.CampaignsConfig",
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",
    'django_extensions'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "food_bank_survey.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'staticfiles'),
            os.path.join(BASE_DIR, "build")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "staticfiles": "django.templatetags.static",
            },
        },
    },
]

WSGI_APPLICATION = "food_bank_survey.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

os.environ["HTTPS"] = "on"

BASE_URL = os.environ.get("BASE_URL", default="localhost:8000")

BASE_WEB_URL = os.environ.get("BASE_WEB_URL", default="localhost")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# The user auth model to leverage
AUTH_USER_MODEL = "users.CampaignUser"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static'),
]

print(STATICFILES_DIRS)
STATIC_ROOT = os.path.join(BASE_DIR, "django_static")
# SECURE_SSL_REDIRECT = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

SWAGGER_SETTINGS = {"USE_SESSION_AUTH": False}

CLOUD_PARTNER = os.environ.get("CLOUD_PARTNER", default="S3")

OBJECT_CONTAINER_NAME = os.environ.get("OBJECT_CONTAINER_NAME", default=None)

ACCESS_KEY = os.environ.get("ACCESS_KEY", default=None)
SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY", default=None)

# ACCOUNT_URL = os.environ.get("ACCOUNT_URL", default=None)

# ACCOUNT_ACCESS_KEY = os.environ.get("ACCOUNT_ACCESS_KEY", default=None)

# ACCOUNT_ACCESS_KEY = os.environ.get("QR_CODE_CONTAINER", default=None)
