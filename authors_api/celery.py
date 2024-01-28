import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.production")

app = Celery("authors_api")

#configure celery app with django setting , namepsaces differentiates the setting for celery and django
app.config_from_object("django.conf:settings", namespace="CELERY")

#discovers the django installed app automatically
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)