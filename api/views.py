from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from main.models import *
from django_page_api.task import task_transaction_test
from celery import group


class PageViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Page.objects.all()
        pagination = PageNumberPagination()
        queryset = pagination.paginate_queryset(queryset, request)
        serializer = PageSerializer(queryset, many=True, context={'request': request})
        return pagination.get_paginated_response(serializer.data)


class PageDetailView(viewsets.ViewSet):

    @transaction.atomic
    def retrieve(self, request, pk=None):
        queryset = Page.objects.all()
        page = get_object_or_404(queryset, pk=pk)
        all_text = page.texts.all()
        all_audios = page.audios.all()
        all_videos = page.videos.all()
        task_transaction_test(all_text)
        task_transaction_test(all_audios)
        task_transaction_test(all_videos)
        serializer = InfoPageSerializer(page)
        return Response(serializer.data)
