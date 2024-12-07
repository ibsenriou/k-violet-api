from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import UserDetailsView

from src.core.serializers.serializer_custom_user import CustomUserSerializer

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomUserDetailView(UserDetailsView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    @action(detail=True)
    def add_points(self, request, pk=None, **kwargs) -> Response:
        """
        Add points and amassed points to the user
        """
        user = self.get_object()
        points = request.data.get('points')

        user.points += points
        user.amassed_points += points
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)