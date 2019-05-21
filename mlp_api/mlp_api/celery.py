import os
from celery import Celery

# set default environment variable to the 'celery' program:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlp_api.settings')

# create celery app and set related module's name ('mlp_api')
app = Celery('mlp_api')

# Configure celery app using django's settings
# 'namespace' argument needs for refference to celery's settings in settings.py
# for example: 'CELERY_BROKER_URL' for message broker
app.config_from_object('django.conf:settings', namespace='CELERY')

# If we need specify task for some django app, we can create 'tasks.py' in app's
# directory, create there required task, and say to celery app find all
# these django-app-specified tasks automatically
app.autodiscover_tasks()
