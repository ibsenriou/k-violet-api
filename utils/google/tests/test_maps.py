import requests
from unittest.mock import Mock

import unittest

from utils.google.maps import Address, MapService, PostalCodeNotFound

GEOCODE_RESULT = {
    "formatted_address": "Rua 13 de Maio, 1 - Centro, Campinas - SP, 13000-000, Brasil",
    "address_components": [
        {
            "long_name": "13000-000",
            "short_name": "13000-000",
            "types": ["postal_code"]
        },
        {
            "long_name": "Rua 13 de Maio",
            "short_name": "Rua 13 de Maio",
            "types": ["route"]
        },
        {
            "long_name": "Centro",
            "short_name": "Centro",
            "types": ["sublocality_level_1", "political"]
        },
        {
            "long_name": "Campinas",
            "short_name": "Campinas",
            "types": ["administrative_area_level_2", "political"]
        },
        {
            "long_name": "São Paulo",
            "short_name": "SP",
            "types": ["administrative_area_level_1", "political"]
        },
        {
            "long_name": "Brazil",
            "short_name": "BR",
            "types": ["country", "political"]
        }
    ]
}


class AddressTests(unittest.TestCase):
    def test_class_init(self):
        address = Address(
            postal_code="13000-000",
            formatted_address="Campinas, SP, Brasil",
            country="Brasil",
            country_code="BR",
            country_three_code="BRA",
            state="São Paulo",
            state_code="SP",
            city="Campinas",
            neighborhood="Centro",
            street="Rua 13 de Maio"
        )

        self.assertEqual(address.postal_code, "13000-000")
        self.assertEqual(address.formatted_address, "Campinas, SP, Brasil")
        self.assertEqual(address.country, "Brasil")
        self.assertEqual(address.country_code, "BR")
        self.assertEqual(address.country_three_code, "BRA")
        self.assertEqual(address.state, "São Paulo")
        self.assertEqual(address.state_code, "SP")
        self.assertEqual(address.city, "Campinas")
        self.assertEqual(address.neighborhood, "Centro")
        self.assertEqual(address.street, "Rua 13 de Maio")

    def test_from_geocode_result(self):
        address = Address.from_geocode_result(GEOCODE_RESULT)

        self.assertEqual(address.postal_code, "13000000")
        self.assertEqual(address.formatted_address,
                         "Rua 13 de Maio, 1 - Centro, Campinas - SP, 13000-000, Brasil")
        self.assertEqual(address.country, "Brasil")
        self.assertEqual(address.country_code, "BR")
        self.assertEqual(address.country_three_code, "BRA")
        self.assertEqual(address.state, "São Paulo")
        self.assertEqual(address.state_code, "SP")
        self.assertEqual(address.city, "Campinas")
        self.assertEqual(address.neighborhood, "Centro")
        self.assertEqual(address.street, "Rua 13 de Maio")

    def test_find_geocode_component_name(self):
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'postal_code'), "13000-000")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'country'), "Brazil")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'country', 'short_name'), "BR")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'administrative_area_level_1'), "São Paulo")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'administrative_area_level_1', 'short_name'), "SP")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'administrative_area_level_2'), "Campinas")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'sublocality_level_1'), "Centro")
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'route'), "Rua 13 de Maio")

    def test_find_geocode_component_name_not_found(self):
        self.assertEqual(Address.find_geocode_component_name(
            GEOCODE_RESULT, 'invalid_key'), None)


class MapServiceTest(unittest.TestCase):

    def test_get_address_on_200(self):
        map_service = MapService()
        map_service.client.geocode = Mock(return_value=[
            GEOCODE_RESULT
        ])

        address = map_service.get_address("13000-000")

        self.assertEqual(address.postal_code, "13000000")
        self.assertEqual(address.formatted_address,
                         "Rua 13 de Maio, 1 - Centro, Campinas - SP, 13000-000, Brasil")
        self.assertEqual(address.country, "Brasil")
        self.assertEqual(address.country_code, "BR")
        self.assertEqual(address.country_three_code, "BRA")
        self.assertEqual(address.state, "São Paulo")
        self.assertEqual(address.state_code, "SP")
        self.assertEqual(address.city, "Campinas")
        self.assertEqual(address.neighborhood, "Centro")
        self.assertEqual(address.street, "Rua 13 de Maio")

    def test_get_address_on_empty_list(self):
        map_service = MapService()
        map_service.client.geocode = Mock(return_value=[])

        with self.assertRaises(PostalCodeNotFound):
            map_service.get_address("13000-000")

    def test_get_address_on_none(self):
        map_service = MapService()
        map_service.client.geocode = Mock(return_value=None)

        with self.assertRaises(PostalCodeNotFound):
            map_service.get_address("13000-000")
