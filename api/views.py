from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from main.models import *
from django_page_api.task import increment_count


# View для получения списка страниц с пагинацией
class PageViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Page.objects.all()
        pagination = PageNumberPagination()
        queryset = pagination.paginate_queryset(queryset, request)
        serializer = PageSerializer(queryset, many=True, context={'request': request})
        return pagination.get_paginated_response(serializer.data)


# View для получения детальной информации о странице
class PageDetailView(viewsets.ViewSet):

    @transaction.atomic
    def retrieve(self, request, pk=None):
        queryset = Page.objects.all()
        page = get_object_or_404(queryset, pk=pk)
        all_text = tuple(page.texts.values_list('id', flat=True))
        all_audios = tuple(page.audios.values_list('id', flat=True))
        all_videos = tuple(page.videos.values_list('id', flat=True))
        if len(all_text) > 0:
            increment_count.delay(all_text, 'Text')
        if len(all_audios) > 0:
            increment_count.delay(all_audios, 'Audio')
        if len(all_videos) > 0:
            increment_count.delay(all_videos, 'Video')
        serializer = InfoPageSerializer(page)
        return Response(serializer.data)
