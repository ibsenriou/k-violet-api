from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.core.views.view_daily_mission import DailyMissionModelViewSet
from src.core.views.view_store_item import StoreItemModelViewSet

router = DefaultRouter()
app_name = 'core'

router.register('daily_missions', DailyMissionModelViewSet, basename='daily_mission')
router.register('store_items', StoreItemModelViewSet, basename='store_item')


urlpatterns = [
    path('', include(router.urls)),
]
