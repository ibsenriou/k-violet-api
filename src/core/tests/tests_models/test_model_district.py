from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_district import District
from utils.factories.core_factories import CoreFactory


class DistrictTest(TestCase):
    def setUp(self) -> None:
        self.city = CoreFactory.create_city()
        self.district = CoreFactory.create_district(fk_city=self.city)

    def test_create_district_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(District, HomespaceBaseModel))

    def test_create_district(self):
        self.assertTrue(District.objects.exists())

    def test_created_district_id_is_uuid(self):
        self.assertTrue(self.district.id, UUID)

    def test_created_district_has_created_at(self):
        self.assertTrue(self.district.created_at)

    def test_created_district_has_updated_at(self):
        self.assertTrue(self.district.updated_at)

    def test_created_district_has_deactivated_at(self):
        self.assertEqual(self.district.deactivated_at, None)

    def test_created_district_deactivated_at_can_be_null(self):
        self.assertTrue(self.district._meta.get_field('deactivated_at').null)

    def test_created_district_has_name(self):
        self.assertEqual(self.district.district_name, 'Center')

    def test_created_district_has_city(self):
        self.assertEqual(self.district.fk_city, self.city)

    def test_district_as_string(self):
        self.assertEqual(str(self.district), 'Center - Campinas')
