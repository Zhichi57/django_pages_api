import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_page_api.settings')
# Настройка Celery для проекта
app = Celery('django_page_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
