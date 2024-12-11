from django.contrib import admin

from src.core.models import StoreItem


@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'image']
    search_fields = ['name']