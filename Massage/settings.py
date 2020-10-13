"""
Django settings for Massage project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*en6h2tuffww*_^vhdyu*($m02cb622t$mu++-j!7lt5*^=f%^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
	ALLOWED_HOSTS = ["*"]
else:
	ALLOWED_HOSTS = ["emassage.top", "www.emassage.top"]
if DEBUG:
    DOMAIN = "127.0.0.1:8000"
else:
    DOMAIN = "www.emassage.top"

# Application definition

INSTALLED_APPS = [
    "grappelli",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "phone_field",
    "rest_framework",
    "corsheaders",
    "main.apps.MainConfig",
    "crispy_forms",
    "django_filters",
    "main.apps.SocialConfig",
    "django_nose",
    "django_inlinecss"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'main.middleware.PathLog',
]

ADMINS = [("Yaroslav", "yariksvitlitskiy81@gmail.com")]

MANAGERS = ADMINS

ROOT_URLCONF = 'Massage.urls'

EXCEPTION_CATCHER = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'main_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': os.path.join(os.getcwd(), 'main.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'main': {
            'handlers': ['main_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'main.context_middlewares.is_authenticated'
            ],
            "libraries":{
                "filterandtag":"main.filterandtag.filters"
            }
        },
    },
]

WSGI_APPLICATION = 'Massage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'massage',
        'USER': 'massage',
        'PASSWORD': 'massage'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/



LOGIN_URL = "/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SERVER_EMAIL = 'yariksvitlitskiy81@gmail.com'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = "emassagemanager@gmail.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "yariksun4002"


LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', _('Russian')),
    ('de', _('German')),
)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "Massage/static/")

MEDIA_ROOT = os.path.join(STATIC_ROOT, "media/")


STATICFILES_DIRS = [
    ("css", os.path.join(STATIC_ROOT, "css/")),
    ("js", os.path.join(STATIC_ROOT, "js/")),
    ("favicon", os.path.join(STATIC_ROOT, "favicon/")),
    ("scrollup", os.path.join(STATIC_ROOT, "scrollup/")),
    ("review", os.path.join(STATIC_ROOT, "review/")),
    ("media", MEDIA_ROOT)
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)




SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "679848365006-gg9qq101pnibpan4uovsehp7g3io0i9r.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "muZEglriskwlOWsp50b7aMAC"


SOCIAL_AUTH_FACEBOOK_KEY = "411250786517398"
SOCIAL_AUTH_FACEBOOK_SECRET = "73e65ffe0b2f2cb034ab2771da00ac82"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_AX_ATTRS = True
SOCIAL_AUTH_GOOGLE_OAUTH2_AX_SCHEMA_ATTRS = [
    ('phonenumber', 'phonenumber')
]

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/user.phonenumbers.read',
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTIFICATION_CLASSES":
        ("rest_framework.authentification.BasicAuthentification",
        "rest_framework.authentification.SessionAuthentification"),
    "DEFAULT_THROTTLE_CLASSES":(
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ),

}


TEST_RUNNER = "django_nose.NoseTestSuiteRunner"


NOSE_ARGS = [
    "--with-coverage",
    "--cover-erase",
    "--cover-inclusive",
    "--cover-package=games"
]
