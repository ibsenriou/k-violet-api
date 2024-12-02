from django.test import TestCase

from src.core.models.model_custom_user import CustomUser
from utils.factories.core_factories import CoreFactory


class CustomUserTest(TestCase):
    def setUp(self) -> None:
        self.user = CoreFactory.create_custom_user()

    def test_create_custom_user(self):
        self.assertTrue(CustomUser.objects.exists())

    def test_created_custom_user_has_email(self):
        self.assertEqual(self.user.email, 'admin@admin.com')

    def test_created_custom_user_has_first_name(self):
        self.assertEqual(self.user.first_name, 'Admin')

    def test_created_custom_user_has_last_name(self):
        self.assertEqual(self.user.last_name, 'Admin')

    def test_created_custom_user_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_created_custom_user_is_staff(self):
        self.assertTrue(self.user.is_staff)

    def test_custom_user_as_string(self):
        self.assertEqual(str(self.user), 'admin@admin.com')
