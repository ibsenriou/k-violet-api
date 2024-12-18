from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.core.views.view_daily_mission import DailyMissionModelViewSet
from src.core.views.view_store_item import StoreItemModelViewSet
from src.core.views.view_user_achievement import UserAchievementView

router = DefaultRouter()
app_name = 'core'

router.register('daily_missions', DailyMissionModelViewSet, basename='daily_mission')
router.register('store_items', StoreItemModelViewSet, basename='store_item')
router.register('user_achievements', UserAchievementView, basename='user_achievement')


urlpatterns = [
    path('', include(router.urls)),
]
