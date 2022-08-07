from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin
from main.models import *


class PageTextsTabularInline(OrderedTabularInline):
    model = PageTextThroughModel
    fields = ('text', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


class PageAudiosTabularInline(OrderedTabularInline):
    model = PageAudiosThroughModel
    fields = ('audio', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


class PageVideosTabularInline(OrderedTabularInline):
    model = PageVideosThroughModel
    fields = ('video', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


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
