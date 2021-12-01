import os
import sys
import random
import string


# Load secret key (generate and store if none exists)

secret_key_path = os.path.dirname(__file__) + "/secretkey.txt"

if os.path.exists(secret_key_path):
    # Read existing secret key
    SECRET_KEY = open(secret_key_path).read().strip()
else:
    # Generate and store secret key
    symbols = string.ascii_letters + string.digits + string.punctuation
    SECRET_KEY = "".join([random.SystemRandom().choice(symbols) for _ in range(50)])
    with open(secret_key_path, "w") as f:
        f.write(SECRET_KEY)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don"t run with debug turned on in production!
if sys.argv[1] == "runserver":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "doc",
    "home",
    "setup",
    "tools",
    "annotate",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "markup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "markup.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation. \
                 UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation. \
                 MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation. \
                 CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation. \
                 NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATA_UPLOAD_MAX_MEMORY_SIZE = None

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,"static")
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR,"static")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,"static")
    ]
