from uuid import UUID
from django.db import IntegrityError
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_year import Year
from utils.factories.core_factories import CoreFactory


class YearTest(TestCase):
    def setUp(self):
        self.year = CoreFactory.create_year(year='2022')

    def test_year_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Year, HomespaceBaseModel))

    def test_create_year(self):
        self.assertTrue(Year.objects.exists)

    def test_created_year_id_is_uuid(self):
        self.assertTrue(self.year.id, UUID)

    def test_created_year_has_created_at(self):
        self.assertTrue(self.year.created_at)

    def test_created_year_has_updated_at(self):
        self.assertTrue(self.year.updated_at)

    def test_created_year_has_deactivated_at(self):
        self.assertEqual(self.year.deactivated_at, None)

    def test_created_year_deactivated_at_can_be_null(self):
        self.assertTrue(self.year._meta.get_field('deactivated_at').null)

    def test_created_year_has_year(self):
        year_description = self.year.year
        self.assertEqual('2022', year_description)

    def test_created_year_as_string(self):
        self.assertEqual('2022', str(self.year))

    def test_created_year_must_be_unique(self):
        with self.assertRaises(Exception) as raised:
            Year.objects.create(year='2022')
        self.assertEqual(IntegrityError, type(raised.exception))
