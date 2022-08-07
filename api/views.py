from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from main.models import *


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
        for text in all_text:
            text.counter = 900

        for text in all_text:
            print(text.counter)
        page.texts.set(all_text)
        serializer = InfoPageSerializer(page)
        return Response(serializer.data)
