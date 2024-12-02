from uuid import UUID
from django.test import TestCase

from src.core.models.model_bank import Bank
from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_color import Color
from utils.factories.core_factories import CoreFactory


class TestBank(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(
            bank_code='0001',
            bank_name='Banco do Brasil'
        )

    def test_bank_exists(self):
        self.assertTrue(Bank.objects.exists())

    def test_bank_extends_abstract_class_homespace_base_model(self):
        self.assertTrue(issubclass(Bank, HomespaceBaseModel))

    def test_bank_has_bank_code(self):
        self.assertEqual(self.bank.bank_code, '0001')

    def test_bank_bank_code_has_to_be_unique(self):
        self.assertTrue(self.bank._meta.get_field('bank_code').unique)

    def test_bank_has_bank_name(self):
        self.assertEqual(self.bank.bank_name, 'Banco do Brasil')

    def test_bank_str_representation(self):
        self.assertEqual(str(self.bank), '0001 - Banco do Brasil')
