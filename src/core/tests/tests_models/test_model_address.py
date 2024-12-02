from uuid import UUID
from django.test import TestCase

from src.core.models.model_homespace_base_model import HomespaceBaseModel
from src.core.models import Address
from utils.factories.core_factories import CoreFactory


class TestAddress(TestCase):
    def setUp(self):
        self.city = CoreFactory.create_city()
        self.cep = CoreFactory.create_postal_code(postal_code_number='13010180	', fk_city=self.city)

        self.address = CoreFactory.create_address(
            fk_postal_code=self.cep,
            street_name='Rua 1',
            number='1',
            complement='Sala 1'
        )

    def test_address_extends_abstract_class_home_space_base_model(self):
        self.assertTrue(issubclass(Address, HomespaceBaseModel))

    def test_create_address(self):
        self.assertTrue(Address.objects.exists())

    def test_created_address_id_is_uuid(self):
        self.assertTrue(self.address.id, UUID)

    def test_created_address_has_created_at(self):
        self.assertTrue(self.address.created_at)

    def test_created_address_has_updated_at(self):
        self.assertTrue(self.address.updated_at)

    def test_created_address_has_deactivated_at(self):
        self.assertEqual(self.address.deactivated_at, None)

    def test_created_address_deactivated_at_can_be_null(self):
        self.assertTrue(self.address._meta.get_field('deactivated_at').null)

    def test_created_address_has_cep(self):
        self.assertEqual(self.address.fk_postal_code, self.cep)

    def test_created_address_has_fk_state(self):
        self.assertTrue(self.address._meta.get_field('fk_state'))

    def test_address_fk_state_can_be_null(self):
        self.assertTrue(Address._meta.get_field('fk_state').null)

    def test_created_address_has_fk_city(self):
        self.assertTrue(self.address._meta.get_field('fk_city'))

    def test_address_fk_city_can_be_null(self):
        self.assertTrue(Address._meta.get_field('fk_city').null)

    def test_created_address_has_fk_district(self):
        self.assertTrue(self.address._meta.get_field('fk_district'))

    def test_address_fk_district_can_be_null(self):
        self.assertTrue(self.address._meta.get_field('fk_district').null)

    def test_created_address_has_street_name(self):
        self.assertEqual(self.address.street_name, 'Rua 1')

    def test_address_street_name_can_be_blank(self):
        self.assertTrue(Address._meta.get_field('street_name').blank)

    def test_created_address_has_number(self):
        self.assertEqual(self.address.number, '1')

    def test_created_address_has_complement(self):
        self.assertEqual(self.address.complement, 'Sala 1')

    def test_address_complement_can_be_blank(self):
        self.assertTrue(Address._meta.get_field('complement').blank)

    def test_address_fk_uhab_can_be_null(self):
        self.assertTrue(Address._meta.get_field('fk_uhab').null)

    def test_address_fk_person_can_be_null(self):
        self.assertTrue(Address._meta.get_field('fk_person').null)

    def test_address_as_str(self):
        self.assertEqual(
            str(self.address),
            str.join(
                ': ',
                (self.address.fk_postal_code.postal_code_number,
                 self.address.street_name, self.address.number)))

    def test_address_has_indexes(self):
        self.assertTrue(self.address._meta.indexes)

    def test_address_has_index_fk_person(self):
        self.assertEqual(self.address._meta.indexes[0].fields, ['fk_person'])

    def test_address_has_index_fk_uhab(self):
        self.assertEqual(self.address._meta.indexes[1].fields, ['fk_uhab'])
