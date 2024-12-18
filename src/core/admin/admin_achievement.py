from django.contrib import admin
from src.core.models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'target_points', 'is_secret']