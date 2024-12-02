import requests
from unittest.mock import Mock

from utils.address_search.service import AddressSearchService

import unittest


class AddressSearchServiceTests(unittest.TestCase):
    def test_get_city_districts_on_200(self):     
        requests.get = Mock(return_value=Mock(status_code=200, json=Mock(
            return_value=[{"state": "SP", "city": "Campinas", "neighborhood": "Centro"}])))
        address_search_service = AddressSearchService()
        districts = address_search_service.get_city_districts("Campinas", "SP")
        self.assertEqual(len(districts), 1)
        self.assertEqual(
            districts[0].city, "Campinas")
        self.assertEqual(
            districts[0].state, "SP")
        self.assertEqual(
            districts[0].neighborhood, "Centro")
        

    def test_get_city_districts_on_404(self):
        requests.get = Mock(return_value=Mock(status_code=404))
        address_search_service = AddressSearchService()
        with self.assertRaises(Exception):
            address_search_service.get_city_districts("Campinas", "SP")

    def test_get_cities_on_200(self):
        requests.get = Mock(return_value=Mock(status_code=200, json=Mock(
            return_value=[{"state": "SP", "city": "Campinas"}])))
        address_search_service = AddressSearchService()
        cities = address_search_service.get_cities("SP")
        self.assertEqual(len(cities), 1)
        self.assertEqual(cities[0].city, "Campinas")
        self.assertEqual(cities[0].state, "SP")

    def test_get_cities_on_404(self):
        requests.get = Mock(return_value=Mock(status_code=404))
        address_search_service = AddressSearchService()
        with self.assertRaises(Exception):
            address_search_service.get_cities("SP")

    def test_get_states_on_200(self):
        requests.get = Mock(return_value=Mock(status_code=200, json=Mock(
            return_value=[{"state": "SP"}])))
        address_search_service = AddressSearchService()
        states = address_search_service.get_states()
        self.assertEqual(len(states), 1)
        self.assertEqual(states[0].state, "SP")

    def test_get_states_on_404(self):
        requests.get = Mock(return_value=Mock(status_code=404))
        address_search_service = AddressSearchService()
        with self.assertRaises(Exception):
            address_search_service.get_states()