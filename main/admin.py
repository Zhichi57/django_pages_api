from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin
from main.models import *


# Inline блок для контента типа текст
class PageTextsTabularInline(OrderedTabularInline):
    model = PageTextThroughModel
    fields = ('text', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


# Inline блок для контента типа аудио
class PageAudiosTabularInline(OrderedTabularInline):
    model = PageAudiosThroughModel
    fields = ('audio', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


# Inline блок для контента типа видео
class PageVideosTabularInline(OrderedTabularInline):
    model = PageVideosThroughModel
    fields = ('video', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


# Изменение страницы редактирование модели Page
class PageAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Page
    list_display = ('title',)

    inlines = (PageTextsTabularInline, PageAudiosTabularInline, PageVideosTabularInline)
    search_fields = (
        'title__startswith', 'videos__title__startswith', 'texts__title__startswith', 'audios__title__startswith')


admin.site.register(Page, PageAdmin)
admin.site.register(Text)
admin.site.register(Video)
admin.site.register(Audio)
