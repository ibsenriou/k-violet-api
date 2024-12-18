from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from src.core.models import UserAchievement
from src.core.serializers.serializer_user_achievement import UserAchievementSerializer


class UserAchievementView(ModelViewSet):
    serializer_class = UserAchievementSerializer
    queryset = UserAchievement.objects.all().order_by('fk_achievement__target_points')

    def get_queryset(self):
        return super().get_queryset().filter(fk_user=self.request.user.id)

    @action(detail=True, methods=['post'])
    def claim(self, request, pk=None):
        user_achievement = get_object_or_404(UserAchievement, pk=pk)

        # Confirm that the user has the coins to claim the achievement
        user = user_achievement.fk_user
        achievement = user_achievement.fk_achievement
        # Don't do anything if the achievement has already been claimed
        if user_achievement.is_claimed:
            return Response({'detail': 'Esta conquista já foi resgatada.'}, status=400)


        if user.amassed_coins < achievement.target_points:
            return Response({'detail': 'Você não possui moedas suficientes para resgatar esta conquista.'},
                            status=400)

        user_achievement.is_claimed = True
        user_achievement.save()
        return Response(self.get_serializer(user_achievement).data)
