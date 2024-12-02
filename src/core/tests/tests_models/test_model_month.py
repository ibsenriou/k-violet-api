from uuid import UUID
from django.db import IntegrityError
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_month import Month
from utils.factories.core_factories import CoreFactory


class MonthTest(TestCase):
    def setUp(self):
        self.month = CoreFactory.create_month()

    def test_month_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Month, HomespaceBaseModel))

    def test_create_month(self):
        self.assertTrue(Month.objects.exists())

    def test_created_month_id_is_uuid(self):
        self.assertTrue(self.month.id, UUID)

    def test_created_month_has_created_at(self):
        self.assertTrue(self.month.created_at)

    def test_created_month_has_updated_at(self):
        self.assertTrue(self.month.updated_at)

    def test_created_month_has_deactivated_at(self):
        self.assertEqual(self.month.deactivated_at, None)

    def test_created_month_deactivated_at_can_be_null(self):
        self.assertTrue(self.month._meta.get_field('deactivated_at').null)

    def test_created_month_has_month_number(self):
        self.assertEqual('01', self.month.month_number)

    def test_created_month_has_month_description(self):
        self.assertEqual('Janeiro', self.month.month_description)

    def test_created_month_has_month_three_chars_abbreviation(self):
        self.assertEqual('Jan', self.month.month_three_chars_abbreviation)

    def test_created_month_has_month_as_string(self):
        self.assertEqual('Janeiro', str(self.month))

    def test_month_number_must_be_unique(self):
        with self.assertRaises(Exception) as raised:
            Month.objects.create(month_number='01')
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_month_description_must_be_unique(self):
        with self.assertRaises(Exception) as raised:
            Month.objects.create(month_description='Janeiro')
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_month_three_chars_abbreviation_must_be_unique(self):
        with self.assertRaises(Exception) as raised:
            Month.objects.create(month_three_chars_abbreviation='Jan')
        self.assertEqual(IntegrityError, type(raised.exception))
