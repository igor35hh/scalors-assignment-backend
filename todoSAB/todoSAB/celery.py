from __future__ import unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoSAB.settings')

app = Celery('foodshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()