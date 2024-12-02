from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import Bank
from src.core.models.model_color import Color
from src.core.serializers.serializer_bank import BankSerializer
from utils.factories.core_factories import CoreFactory
from src.core.serializers.serializer_color import ColorSerializer
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

BANK_URL = reverse_lazy('core:bank-list')


class PublicBankAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(BANK_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateBankAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.bank = Bank.objects.create(bank_code = '0001', bank_name = 'Banco do Brasil')
        self.bank2 = Bank.objects.create(bank_code = '0002', bank_name = 'Banco Itaú')

        # Queryset objects and pass to the serializer.
        self.banks = Bank.objects.all().order_by('bank_code')
        self.serializer = BankSerializer(self.banks, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(BANK_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_banks(self):
        banks_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(banks_list_results, self.serializer.data)

    def test_retrieve_first_bank_name(self):
        first_bank_name_from_response_data_results = self.response.data['results'][0]['bank_name']
        first_bank_name_from_list_serializer_data = self.serializer.data[0]['bank_name']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_bank_name_from_response_data_results,
                         first_bank_name_from_list_serializer_data)