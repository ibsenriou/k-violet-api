from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.core.views.view_daily_mission import DailyMissionModelViewSet

router = DefaultRouter()
app_name = 'core'

router.register('daily_missions', DailyMissionModelViewSet, basename='daily_mission')


urlpatterns = [
    path('', include(router.urls)),
]
