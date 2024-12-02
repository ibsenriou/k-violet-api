from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.core.models.model_custom_user import CustomUser
from src.core.models.model_custom_user import CustomUserManager


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        # Use the custom form for user creation and editing
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def save_model(self, request, obj, form, change):
        # Use the custom user manager to create and save the user
        obj.save()

    def create_user(self, request, email, first_name, last_name, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        manager = CustomUserManager()
        user = manager.create_user(email, password=password, first_name=first_name, last_name=last_name, **extra_fields)
        return user
