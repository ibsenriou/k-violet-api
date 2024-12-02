from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models import City
from utils.factories.core_factories import CoreFactory


class TestCity(TestCase):
    def setUp(self):
        self.country = CoreFactory.create_country(country_name='Brasil', country_two_digits_code='BR',
                                                  country_three_digits_code='BRA')
        self.state = CoreFactory.create_state()
        self.city = CoreFactory.create_city()

    def test_city_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(City, HomespaceBaseModel))

    def test_create_city(self):
        self.assertTrue(City.objects.exists())

    def test_created_city_id_is_uuid(self):
        self.assertTrue(self.city, UUID)

    def test_created_city_has_created_at(self):
        self.assertTrue(self.city.created_at)

    def test_created_city_has_updated_at(self):
        self.assertTrue(self.city.updated_at)

    def test_created_city_has_deactivated_at(self):
        self.assertEqual(self.city.deactivated_at, None)

    def test_created_city_deactivated_at_can_be_null(self):
        self.assertTrue(self.city._meta.get_field('deactivated_at').null)

    def test_created_city_has_fk_state(self):
        self.assertEqual(self.city.fk_state, self.state)

    def test_created_city_has_city_name(self):
        self.assertEqual(self.city.city_name, 'Campinas')

    def test_city_as_str(self):
        self.assertEqual(str(self.city), 'Campinas')
