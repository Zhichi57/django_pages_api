from django.contrib import admin
from main.models import *


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = (
        'title__startswith', 'videos__title__startswith', 'texts__title__startswith', 'audios__title__startswith')
