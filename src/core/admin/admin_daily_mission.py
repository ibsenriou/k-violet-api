from django.contrib import admin

from src.core.models import DailyMission


@admin.register(DailyMission)
class DailyMissionAdmin(admin.ModelAdmin):
    # If user is superuser, show all daily missions else show only user's daily missions
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(fk_user=request.user.id)

    # If user is superuser, allow to change fk_user else disable it
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ['fk_user']

    # If user is superuser, allow to add daily mission else disable it
    def has_add_permission(self, request):
        return request.user.is_superuser

    list_display = ['id', 'description', 'points', 'is_completed', 'target_date', 'fk_user']
    list_filter = ['is_completed', 'target_date']
    search_fields = ['description']
    ordering = ['target_date']
    actions = ['complete_mission']

    def complete_mission(self, request, queryset):
        queryset.update(is_completed=True)
        for mission in queryset:
            mission.complete_mission()
    complete_mission.short_description = 'Completar missão'
    complete_mission.allowed_permissions = ('change',)
