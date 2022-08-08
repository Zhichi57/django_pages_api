from celery import shared_task
from django.db import transaction
from main.models import Text, Audio, Video


# Задача для увелечения счетчика просмотра
@shared_task()
def increment_count(objects, content_type):
    with transaction.atomic():
        if content_type == 'Text':
            objects_list = Text.objects.filter(id__in=objects)
        elif content_type == 'Audio':
            objects_list = Audio.objects.filter(id__in=objects)
        else:
            objects_list = Video.objects.filter(id__in=objects)
        for obj in objects_list:
            obj.counter = obj.counter + 1
            obj.save()
    return True
