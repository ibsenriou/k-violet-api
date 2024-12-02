from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_measurement_unit import MeasurementUnit
from utils.factories.core_factories import CoreFactory


class MeasurementUnitTest(TestCase):
    def setUp(self):
        self.measurement_unit = CoreFactory.create_measurement_unit()

    def test_measurement_unit_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(MeasurementUnit, HomespaceBaseModel)

    def test_create_measurement_unit(self):
        self.assertTrue(MeasurementUnit.objects.exists)

    def test_created_measurement_unit_id_is_uuid(self):
        self.assertTrue(self.measurement_unit.id, UUID)

    def test_created_measurement_unit_has_created_at(self):
        self.assertTrue(self.measurement_unit.created_at)

    def test_created_measurement_unit_has_updated_at(self):
        self.assertTrue(self.measurement_unit.updated_at)

    def test_created_measurement_unit_has_deactivated_at(self):
        self.assertEqual(self.measurement_unit.deactivated_at, None)

    def test_created_measurement_unit_deactivated_at_can_be_null(self):
        self.assertTrue(self.measurement_unit._meta.get_field('deactivated_at').null)

    def test_measurement_unit_has_character_abbreviation(self):
        self.assertEqual('KWH', self.measurement_unit.character_abbreviation)

    def test_measurement_unit_has_description(self):
        self.assertEqual('KiloWatt', self.measurement_unit.description)

    def test_measurement_unit_as_str(self):
        self.assertEqual('KiloWatt: KWH', str(self.measurement_unit))
