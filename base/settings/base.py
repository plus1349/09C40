from pathlib import Path
from os import environ

from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent

try:
    SECRET_KEY = environ["SECRET_KEY"]
except KeyError as exception:
    raise KeyError("Environment valiable SECRET_KEY isn't set!") from exception

DEBUG = False

ALLOWED_HOSTS = ()

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "abilities",
)

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
)

ROOT_URLCONF = "base.urls"

TEMPLATES = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (BASE_DIR / "templates",),
        "APP_DIRS": True,
        "OPTIONS": {
            "libraries": {
                "base": "base.templatetags",
            },
            "context_processors": (
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ),
        },
    },
)

ASGI_APPLICATION = "base.asgi.application"
WSGI_APPLICATION = "base.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "09C40.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = (
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
)

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uk", _("Ukrainian")),
)

LOCALE_PATHS = (BASE_DIR / "locale",)

TIME_ZONE = "Europe/Kiev"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

STATICFILES_DIRS = (BASE_DIR / "static",)
STATIC_ROOT = ROOT_DIR / "staticfiles"
STATIC_URL = "/static/"

LOG_DIR = BASE_DIR / "logs"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.request": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\n[{server_time}] {message}",
            "style": "{",
        },
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "django.request": {
            "backupCount": 10240,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.__str__() + "/django/request/request.log",
            "formatter": "django.request",
            "level": "ERROR",
            "maxBytes": 10485760,
        },
        "django.server": {
            "backupCount": 10240,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.__str__() + "/django/server/server.log",
            "formatter": "django.server",
            "level": "INFO",
            "maxBytes": 10485760,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ("django.request",),
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ("django.server",),
            "level": "INFO",
            "propagate": False,
        },
    },
}
