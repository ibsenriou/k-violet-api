from uuid import UUID
import datetime

from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_period import Period
from utils.factories.core_factories import CoreFactory


class PeriodTest(TestCase):
    def setUp(self):
        self.year = CoreFactory.create_year()
        self.month = CoreFactory.create_month()
        self.period = CoreFactory.create_period()

    def test_period_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Period, HomespaceBaseModel))

    def test_create_period(self):
        self.assertTrue(Period.objects.exists())

    def test_created_period_id_is_uuid(self):
        self.assertTrue(self.period.id, UUID)

    def test_created_has_created_at(self):
        self.assertTrue(self.period.created_at)

    def test_created_period_has_updated_at(self):
        self.assertTrue(self.period.updated_at)

    def test_created_period_has_deactivated_at(self):
        self.assertEqual(self.period.deactivated_at, None)

    def test_created_period_deactivated_at_can_be_null(self):
        self.assertTrue(self.period._meta.get_field('deactivated_at').null)

    def test_created_period_has_period_code(self):
        self.assertEqual('2023.01', self.period.period_code)

    def test_created_period_has_start_date(self):
        start_date = self.period.start_date
        self.assertEqual(datetime.date(2023, 1, 1), start_date)

    def test_created_period_has_end_date(self):
        end_date = self.period.end_date
        self.assertEqual(datetime.date(2023, 1, 31), end_date)

    def test_created_period_has_fk_year(self):
        self.assertEqual(self.year, self.period.fk_year)

    def test_created_period_has_fk_month(self):
        self.assertEqual(self.month, self.period.fk_month)

    def test_created_period_has_fk_period_previous_period(self):
        self.assertTrue(self.period._meta.get_field('fk_period_previous_period'))

    def test_created_period_previous_period_can_be_blank(self):
        previous_period = self.period._meta.get_field('fk_period_previous_period')
        self.assertTrue(previous_period.blank)

    def test_created_period_has_fk_period_next_period(self):
        self.assertTrue(self.period._meta.get_field('fk_period_next_period'))

    def test_created_period_next_period_can_be_blank(self):
        next_period = self.period._meta.get_field('fk_period_next_period')
        self.assertTrue(next_period.blank)

    def test_period_as_str(self):
        self.assertEqual('2023.01', str(self.period))
