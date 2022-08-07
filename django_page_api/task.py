from celery import group
from celery import shared_task
from django.db import transaction


@shared_task()
def task_transaction_test(objects):
    with transaction.atomic():
        for obj in objects:
            obj.counter = obj.counter + 1
            obj.save()
