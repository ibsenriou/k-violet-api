import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from src.core.models import DailyMission
from src.core.serializers.serializer_daily_mission import DailyMissionSerializer


class DailyMissionModelViewSet(viewsets.ModelViewSet):
    serializer_class = DailyMissionSerializer
    queryset = DailyMission.objects.all().order_by('-id')

    def get_queryset(self):
        return super().get_queryset().filter(fk_user=self.request.user.id, target_date=datetime.date.today())

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        if not pk:
            return Response({'status': 'Mission not found'}, status=404)

        if request.user != self.get_object().fk_user:
            return Response({'status': 'You do not have permission to complete this mission'}, status=403)

        if self.get_object().is_completed:
            return Response({'status': 'Mission already completed'}, status=400)

        mission = self.get_object()
        mission.complete_mission()

        return Response({'status': 'Mission completed'})