from .base import * #noqa #to ignore this 
from .base import envs

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=envs(
    "DJANGO_SECRET_KEY",
    default="P3furfn2LTNdBmllzE-LXsaLXNqXpx3w--RqBDU90y8HlBatTgc",
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = envs("EMAIL_HOST", default="mailhog")
EMAIL_PORT = envs("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "ganeshchile0307@gmail.com"
DOMAIN = envs("DOMAIN")
SITE_NAME = "Project1"
