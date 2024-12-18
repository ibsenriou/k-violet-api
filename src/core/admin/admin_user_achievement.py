from django.contrib import admin
from src.core.models import UserAchievement

@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['fk_user', 'fk_achievement', 'is_claimed']