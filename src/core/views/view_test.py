from rest_framework import viewsets

from src.core.models import Test
from src.core.serializers.serializer_test import TestSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer