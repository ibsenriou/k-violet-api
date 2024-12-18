from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import StoreItem, CustomUser
from src.core.serializers.serializer_store_item import StoreItemSerializer
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

STORE_ITEM_URL = reverse_lazy('core:store_item-list')


class StoreItemAPITests(TestCase):
    def setUp(self):
        # Initialize APIClient
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(STORE_ITEM_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateStoreItemAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Call parent setup
        super().setUp()

        ### SETUP ###
        self.user = CustomUser.objects.get(email='admin@admin.com')

        # Create mock StoreItem instances
        self.store_items = [
            StoreItem.objects.create(
                name='Vale Doce',
                cost=300,
                image='/images/little-store/icons/candy2.webp'
            ),
            StoreItem.objects.create(
                name='Vale Brinquedo',
                cost=500,
                image='/images/little-store/icons/toy2.webp'
            ),
        ]

        # Queryset objects and pass to the serializer
        self.store_item_queryset = StoreItem.objects.all().order_by('id')
        self.serializer = StoreItemSerializer(self.store_item_queryset, many=True)

        # Makes API call to get the Response
        self.response = self.client.get(STORE_ITEM_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_store_items(self):
        store_item_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(store_item_list_results, self.serializer.data)

    def test_retrieve_first_store_item_name(self):
        first_item_name_results = self.response.data['results'][0]['name']
        first_item_name_data = self.serializer.data[0]['name']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_item_name_results, first_item_name_data)
