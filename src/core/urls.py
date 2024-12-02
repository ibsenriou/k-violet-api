from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.core.views.view_test import TestModelViewSet

router = DefaultRouter()
app_name = 'core'

router.register('test', TestModelViewSet, basename='test')


urlpatterns = [
    path('', include(router.urls)),
]
