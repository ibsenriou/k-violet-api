from rest_framework import serializers

from src.core.models import DailyMission


class DailyMissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyMission
        fields = '__all__'
