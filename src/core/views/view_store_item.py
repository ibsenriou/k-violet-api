from rest_framework.viewsets import ModelViewSet
from src.core.models import StoreItem
from src.core.serializers.serializer_store_item import StoreItemSerializer

from rest_framework.response import Response
from rest_framework.decorators import action

class StoreItemModelViewSet(ModelViewSet):
    queryset = StoreItem.objects.all().order_by('cost')
    serializer_class = StoreItemSerializer

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        if not pk:
            return Response({'status': 'Item not found'}, status=404)

        item = self.get_object()
        user = request.user

        if user.coins < item.cost:
            return Response({'status': 'Not enough coins'}, status=400)

        user.coins -= item.cost
        user.save()

        return Response({'status': 'Item bought'}, status=200)