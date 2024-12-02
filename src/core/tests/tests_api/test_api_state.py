from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from src.core.models import State
from src.core.serializers.serializer_state import StateSerializer
from utils.factories.core_factories import CoreFactory
from utils.test_setups.authenticated_api_test_case import AuthenticatedAPITestCase

STATE_URL = reverse_lazy('core:state-list')


class PublicStateAPITests(TestCase):
    def setUp(self):
        # Initiate APIClient and setUp test Database.
        self.client = APIClient()

    def test_login_required(self):
        response = self.client.get(STATE_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateStateAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        # Initiate super() and setUp test Database.
        super().setUp()

        self.state = CoreFactory.create_state()

        # Queryset objects and pass to the serializer.
        self.states = State.objects.all().order_by('-id')
        self.serializer = StateSerializer(self.states, many=True)

        # Makes API call to get the Response.
        self.response = self.client.get(STATE_URL)

    def tearDown(self):
        super().tearDown()

    def test_retrieve_states(self):
        states_list_results = self.response.data['results']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(states_list_results, self.serializer.data)

    def test_retrieve_first_states_name(self):
        first_state_name_from_response_data_results = self.response.data['results'][0]['state_name']
        first_state_name_from_list_serializer_data = self.serializer.data[0]['state_name']

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_state_name_from_response_data_results,
                         first_state_name_from_list_serializer_data)
