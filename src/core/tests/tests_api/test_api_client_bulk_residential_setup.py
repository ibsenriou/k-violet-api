from django.test import TestCase
from rest_framework.exceptions import ValidationError

from src.core.serializers.custom_serializers.serializer_client_bulk_residential_setup import \
    ClientBulkResidentialSetupSerializer
from utils.factories.condominium_factories import CondominiumFactory
from utils.factories.lookup_factories import LookupFactory


class ClientBulkResidentialSetupSerializerTestCase(TestCase):
    def setUp(self):
        # Create some test data
        self.condominium = CondominiumFactory.create_condominium(name="Test Condominium")
        self.grouping_type = LookupFactory.create_lookup_type_of_condominium_grouping(description="Blocks")
        self.residential_type = LookupFactory.create_lookup_type_of_residential(description="Apartment")
        self.grouping = CondominiumFactory.create_condominium_grouping(
            name="A", fk_uhab=self.condominium, fk_lookup_type_of_condominium_grouping=self.grouping_type, fk_condominium_id=self.condominium.id
        )

    def test_valid_data(self):
        # Test serializer with valid data
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "A",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '101,102,103,'
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        # Test serializer with invalid data
        invalid_data = {
            'fk_condominium': 'invalid_id',
            'fk_lookup_type_of_condominium_grouping': 'invalid_id',
            'fk_lookup_type_of_residential': 'invalid_id',
            'residential_units': [['Unit1', 'Unit2'], ['Unit3']]
        }
        serializer = ClientBulkResidentialSetupSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_create_residential_units(self):
        # Test creation of residential units
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "A",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '101,102,103'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.grouping.get_residentials().count(), 3)

    def test_create_residential_units_without_grouping(self):
        # Test creation of residential units without grouping
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '101,102,103'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.condominium.get_condominium_residentials().count(), 3)

    def test_creating_more_residentials_in_same_grouping_dont_generate_duplicate_condominium_grouping(self):
        # Test creation of residential units without grouping
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "A",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '101,102,103'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.condominium.get_condominium_groupings().count(), 1)
        self.assertEqual(self.condominium.get_condominium_residentials().count(), 3)

        # Test creation of residential units without grouping
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "A",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '104,105,106'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.condominium.get_condominium_groupings().count(), 1)
        self.assertEqual(self.condominium.get_condominium_residentials().count(), 6)

    def test_create_residentials_in_more_than_one_grouping(self):
        # Test creation of residential units without grouping
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "A",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '101,102,103'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.condominium.get_condominium_groupings().count(), 1)
        self.assertEqual(self.condominium.get_condominium_residentials().count(), 3)

        # Test creation of residential units without grouping
        data = {
            'fk_condominium': str(self.condominium.id),
            'fk_lookup_type_of_condominium_grouping': str(self.grouping_type.id),
            'condominium_grouping_description': "B",
            'fk_lookup_type_of_residential': str(self.residential_type.id),
            'residential_units': '104,105,106'  # 3 residential units
        }
        serializer = ClientBulkResidentialSetupSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)

        # Assert that residential units were created
        self.assertEqual(self.condominium.get_condominium_groupings().count(), 2)
        self.assertEqual(self.condominium.get_condominium_residentials().count(), 6)
