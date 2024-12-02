from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import City
from src.core.serializers.serializer_city import CitySerializer
from utils.factories.core_factories import CoreFactory
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

CITY_URL = reverse_lazy('core:city-list')


class PublicCityAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(CITY_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateCityAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.city = CoreFactory.create_city()

        # Queryset objects and pass to the serializer.
        self.cities = City.objects.all().order_by('-id')
        self.serializer = CitySerializer(self.cities, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(CITY_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_cities(self):
        cities_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(cities_list_results, self.serializer.data)

    def test_retrieve_first_city_name(self):

        first_city_name_from_response_data_results = self.response.data['results'][0]['city_name']
        first_city_name_from_list_serializer_data = self.serializer.data[0]['city_name']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_city_name_from_response_data_results,
                         first_city_name_from_list_serializer_data)
