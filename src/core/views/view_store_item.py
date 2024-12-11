from rest_framework.viewsets import ModelViewSet
from src.core.models import StoreItem
from src.core.serializers.serializer_store_item import StoreItemSerializer

class StoreItemModelViewSet(ModelViewSet):
    queryset = StoreItem.objects.all().order_by('-id')
    serializer_class = StoreItemSerializer
