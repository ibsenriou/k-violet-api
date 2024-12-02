from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models.model_color import Color
from utils.factories.core_factories import CoreFactory
from src.core.serializers.serializer_color import ColorSerializer
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

COLOR_URL = reverse_lazy('core:color-list')


class PublicColorAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(COLOR_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateColorAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.color_white = CoreFactory.create_color(description='White')
        self.color_black = CoreFactory.create_color(description='Black')
        self.color_yellow = CoreFactory.create_color(description='Yellow')

        # Queryset objects and pass to the serializer.
        self.colors = Color.objects.all().order_by('description')
        self.serializer = ColorSerializer(self.colors, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(COLOR_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_colors(self):
        colors_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(colors_list_results, self.serializer.data)

    def test_retrieve_first_colors_name(self):
        first_color_name_from_response_data_results = self.response.data['results'][0]['description']
        first_color_name_from_list_serializer_data = self.serializer.data[0]['description']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_color_name_from_response_data_results,
                         first_color_name_from_list_serializer_data)
