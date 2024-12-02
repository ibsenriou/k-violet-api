from rest_framework import serializers

from src.core.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = 'id', 'email', 'first_name', 'last_name', 'is_active', 'user_roles'
