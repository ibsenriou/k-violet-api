import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import DailyMission, CustomUser
from src.core.serializers.serializer_daily_mission import DailyMissionSerializer
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

DAILY_MISSION_URL = reverse_lazy('core:daily_mission-list')


class DailyMissionAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(DAILY_MISSION_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateDailyMissionAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        ### SETUP ###
        self.user = CustomUser.objects.get(email='admin@admin.com')
        self.mission = DailyMission.objects.create(
            description='Comprar um café',
            points=10,
            is_completed=False,
            target_date=datetime.date.today(),
            fk_user=self.user
        )

        # Queryset objects and pass to the serializer.
        self.daily_missions = DailyMission.objects.all().order_by('-id')
        self.serializer = DailyMissionSerializer(self.daily_missions, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(DAILY_MISSION_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_daily_missions(self):
        daily_mission_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(daily_mission_list_results, self.serializer.data)

    def test_retrieve_first_daily_mission_description(self):
        first_mission_description_results = self.response.data['results'][0]['description']
        first_mission_description_data = self.serializer.data[0]['description']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_mission_description_results, first_mission_description_data)
