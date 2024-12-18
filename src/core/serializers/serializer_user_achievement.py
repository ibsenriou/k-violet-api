from rest_framework import serializers
from src.core.models import UserAchievement, Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class UserAchievementSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.SerializerMethodField()
    achievement = AchievementSerializer(source='fk_achievement', read_only=True)
    progress = serializers.SerializerMethodField()

    class Meta:
        model = UserAchievement
        fields = ['id', 'fk_achievement', 'achievement', 'fk_user', 'progress', 'progress_percentage', 'is_claimed']

    def get_progress(self, obj):
        user = obj.fk_user
        user_amassed_coins = user.amassed_coins

        achievement = obj.fk_achievement
        achievement_target_points = achievement.target_points
        return min(user_amassed_coins, achievement_target_points)


    def get_progress_percentage(self, obj):
        user = obj.fk_user
        achievement = obj.fk_achievement

        user_amassed_coins = user.amassed_coins
        achievement_target_points = achievement.target_points

        return min(100, (user_amassed_coins / achievement_target_points) * 100)
