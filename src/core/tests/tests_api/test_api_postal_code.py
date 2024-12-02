from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient
from unittest.mock import Mock

from src.core.models import PostalCode
from src.core.serializers.serializer_postal_code import PostalCodeSerializer
from utils.factories.core_factories import CoreFactory
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase
from src.core.views.view_postal_code import PostalCodeModelViewSet


POSTAL_CODE_URL = reverse_lazy('core:postal_code-list')


class PublicPostalCodeAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(POSTAL_CODE_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivatePostalCodeAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.postal_code = CoreFactory.create_postal_code()

        # Queryset objects and pass to the serializer.
        self.postal_codes = PostalCode.objects.all().order_by('-id')
        self.serializer = PostalCodeSerializer(self.postal_codes, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(POSTAL_CODE_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_postal_codes(self):
        postal_codes_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(postal_codes_list_results, self.serializer.data)

    def test_retrieve_first_postal_code_number_of_postal_code(self):
        first_postal_code_number_of_postal_code_from_response_data_results = (
            self.response.data)['results'][0]['postal_code_number']
        first_postal_code_number_of_postal_code_from_list_serializer_data = (
            self.serializer.data)[0]['postal_code_number']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_postal_code_number_of_postal_code_from_response_data_results,
                         first_postal_code_number_of_postal_code_from_list_serializer_data)

    def test_list_unregistered_postal_code_with_all_address_info(self):        
        PostalCodeModelViewSet.map_service.get_address = Mock(
            return_value=CoreFactory.create_google_address("89255720"))
        
        url_with_unregistered_postal_code = reverse_lazy(
            'core:postal_code-list') + '?postal_code_number=89255720'
        response = self.client.get(url_with_unregistered_postal_code)

        created_postal_code = PostalCode.objects.get(postal_code_number='89255720')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['postal_code_number'], created_postal_code.postal_code_number)
        
    def test_list_unregistered_postal_code_without_street_and_district_info(self):
        PostalCodeModelViewSet.map_service.get_address = Mock(
            return_value=CoreFactory.create_google_address_without_street_and_district_info("89255721"))
        
        PostalCodeModelViewSet.address_search_service.get_city_districts = Mock(
            return_value=CoreFactory.create_address_search_districts())
        
        url_with_unregistered_postal_code = reverse_lazy(
            'core:postal_code-list') + '?postal_code_number=89255721'
        
        response = self.client.get(url_with_unregistered_postal_code)

        created_postal_code = PostalCode.objects.get(postal_code_number='89255721')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['postal_code_number'], created_postal_code.postal_code_number)
        self.assertEqual(response.data['results'][0]['fk_district'], None)