from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import Address
from src.core.serializers.serializer_address import AddressSerializer
from utils.factories.core_factories import CoreFactory
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

ADDRESS_URL = reverse_lazy('core:address-list')


class PublicAddressAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(ADDRESS_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateAddressAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.address = CoreFactory.create_address()

        # Queryset objects and pass to the serializer.
        self.addresses = Address.objects.all().order_by('-id')
        self.serializer = AddressSerializer(self.addresses, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(ADDRESS_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_addresses(self):
        addresses_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(addresses_list_results, self.serializer.data)

    def test_retrieve_first_address_postal_code(self):
        first_address_postal_code_from_response_data_results = self.response.data['results'][0]['fk_postal_code']
        first_address_postal_code_from_list_serializer_data = self.serializer.data[0]['fk_postal_code']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_address_postal_code_from_response_data_results,
                         first_address_postal_code_from_list_serializer_data)
