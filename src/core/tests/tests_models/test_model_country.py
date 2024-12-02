from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_country import Country
from utils.factories.core_factories import CoreFactory


class TestCountry(TestCase):
    def setUp(self):
        self.country = CoreFactory.create_country(
            country_two_digits_code='BR',
            country_name='Brasil',
            country_three_digits_code='BRA'
        )

    def test_country_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Country, HomespaceBaseModel))

    def test_create_country(self):
        self.assertTrue(Country.objects.exists())

    def test_created_country_id_is_uuid(self):
        self.assertTrue(self.country.id, UUID)

    def test_created_country_has_created_at(self):
        self.assertTrue(self.country.created_at)

    def test_created_country_has_updated_at(self):
        self.assertTrue(self.country.updated_at)

    def test_created_country_has_deactivated_at(self):
        self.assertEqual(self.country.deactivated_at, None)

    def test_created_country_deactivated_at_can_be_null(self):
        self.assertTrue(self.country._meta.get_field('deactivated_at').null)

    def test_created_country_has_country_two_digits_code(self):
        self.assertEqual(self.country.country_two_digits_code, 'BR')

    def test_created_country_has_country_three_digits_code(self):
        self.assertEqual(self.country.country_three_digits_code, 'BRA')

    def test_created_country_has_country_name(self):
        self.assertEqual(self.country.country_name, 'Brasil')

    def test_country_as_string(self):
        self.assertEqual(str(self.country), 'Brasil')
