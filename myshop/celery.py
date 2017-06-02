import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

# Create an instance of our application
app = Celery('myshop')
# Load any custom config from our project settings
app.config_from_object('django.conf:settings')
# Autodiscover asynchronous task for apps listed in INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
