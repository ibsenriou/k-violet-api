from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_color import Color
from utils.factories.core_factories import CoreFactory


class TestColor(TestCase):
    def setUp(self):
        self.color = CoreFactory.create_color(description='Violeta')

    def test_color_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Color, HomespaceBaseModel))

    def test_create_color(self):
        self.assertTrue(Color.objects.exists())

    def test_created_color_id_is_uuid(self):
        self.assertTrue(self.color.id, UUID)

    def test_created_color_has_created_at(self):
        self.assertTrue(self.color.created_at)

    def test_created_color_has_updated_at(self):
        self.assertTrue(self.color.updated_at)

    def test_created_color_has_deactivated_at(self):
        self.assertEqual(self.color.deactivated_at, None)

    def test_created_color_deactivated_at_can_be_null(self):
        self.assertTrue(self.color._meta.get_field('deactivated_at').null)

    def test_created_color_has_description(self):
        self.assertEqual(self.color.description, 'Violeta')

    def test_created_color_description_is_unique(self):
        unique_constraint = self.color._meta.get_field('description').unique
        self.assertTrue(unique_constraint)

    def test_created_color_str(self):
        self.assertTrue(str(self.color), 'Violeta')
