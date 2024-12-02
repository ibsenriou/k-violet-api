from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models.model_postal_code import PostalCode
from utils.factories.core_factories import CoreFactory
from utils.google.maps import Address


class CepTest(TestCase):
    def setUp(self) -> None:
        self.city = CoreFactory.create_city()
        self.district = CoreFactory.create_district()
        self.postal_code = CoreFactory.create_postal_code(postal_code_number='13840000',
                                                          fk_city=self.city,
                                                          fk_district=self.district,
                                                          street_name='Rua Teste')

    def test_postal_code_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(PostalCode, HomespaceBaseModel))

    def test_create_postal_code(self):
        self.assertTrue(PostalCode.objects.exists())

    def test_created_postal_code_id_is_uuid(self):
        self.assertTrue(self.postal_code.id, UUID)

    def test_created_postal_code_has_created_at(self):
        self.assertTrue(self.postal_code.created_at)

    def test_created_postal_code_has_updated_at(self):
        self.assertTrue(self.postal_code.updated_at)

    def test_created_postal_code_has_deactivated_at(self):
        self.assertEqual(self.postal_code.deactivated_at, None)

    def test_created_postal_code_deactivated_at_can_be_null(self):
        self.assertTrue(self.postal_code._meta.get_field('deactivated_at').null)

    def test_created_postal_code_has_postal_code_number(self):
        self.assertEqual(self.postal_code.postal_code_number, '13840000')

    def test_created_postal_code_has_fk_city(self):
        self.assertEqual(self.postal_code.fk_city, self.city)

    def test_created_postal_code_has_fk_district(self):
        self.assertEqual(self.postal_code.fk_district, self.district)

    def test_postal_code_fk_district_can_be_null(self):
        self.assertTrue(self.postal_code._meta.get_field('fk_district').null)

    def test_created_postal_code_has_street_name(self):
        self.assertEqual(self.postal_code.street_name, 'Rua Teste')

    def test_postal_code_street_name_can_be_blank(self):
        self.assertTrue(self.postal_code._meta.get_field('street_name').blank)

    def test_postal_code_as_string(self):
        self.assertEqual(str(self.postal_code), self.postal_code.postal_code_number)

    def test_create_postal_code_by_address(self):
        address = Address()
        address.postal_code = '13840001'
        address.formatted_address = 'Rua Teste, 123'
        address.country = 'Brasil'
        address.country_code = 'BR'
        address.country_three_code = 'BRA'
        address.state = 'São Paulo'
        address.state_code = 'SP'
        address.city = 'Campinas'
        address.neighborhood = 'Centro'
        address.street = 'Rua Teste'
        
        PostalCode.create_postal_code(address)

        postal_code = PostalCode.objects.get(postal_code_number='13840001')
        self.assertEqual(postal_code.postal_code_number, '13840001')
        self.assertEqual(postal_code.fk_city.city_name, 'Campinas')
        self.assertEqual(postal_code.fk_district.district_name, 'Centro')
        self.assertEqual(postal_code.street_name, 'Rua Teste')

        