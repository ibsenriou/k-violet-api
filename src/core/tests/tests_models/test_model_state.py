from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_state import State
from utils.factories.core_factories import CoreFactory


class TestState(TestCase):
    def setUp(self):
        self.country = CoreFactory.create_country(
            country_name='Brasil', country_two_digits_code='BR', country_three_digits_code='BRA'
        )
        self.state = CoreFactory.create_state()

    def test_state_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(State, HomespaceBaseModel))

    def test_create_state(self):
        self.assertTrue(State.objects.exists())

    def test_created_state_id_is_uuid(self):
        self.assertTrue(self.state.id, UUID)

    def test_created_state_has_created_at(self):
        self.assertTrue(self.state.created_at)

    def test_created_state_has_updated_at(self):
        self.assertTrue(self.state.updated_at)

    def test_created_state_has_deactivated_at(self):
        self.assertEqual(self.state.deactivated_at, None)

    def test_created_state_deactivated_at_can_be_null(self):
        self.assertTrue(self.state._meta.get_field('deactivated_at').null)

    def test_created_state_has_fk_country(self):
        self.assertEqual(self.state.fk_country, self.country)

    def test_created_state_has_state_two_digits_code(self):
        self.assertEqual(self.state.state_two_digits_code, 'SP')

    def test_created_state_has_state_name(self):
        self.assertEqual(self.state.state_name, 'São Paulo')

    def test_state_as_str(self):
        self.assertEqual(str(self.state), 'São Paulo')
