from .base import *

EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_USE_TILS= True
EMAIL_HOST_USER= env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL= "pnakitaren2@gmail.com"
DOMAIN=env("DOMAIN")
SITE_NAME= "Real Estate"
EMAIL_PORT=env("EMAIL_PORT")

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PORT': env("PG_PORT"),
    }
}