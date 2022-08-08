from django.urls import path, include
from api.views import *


urlpatterns = [
    path('pages/', PageViewSet.as_view({'get': 'list'}), name='page-list'),
    path('pages/<int:pk>/', PageDetailView.as_view({'get': 'retrieve'}), name='page-detail')
]
