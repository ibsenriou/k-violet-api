from typing import List
from django.conf import settings

import requests


class State:
    state: str

    def __init__(self, state: str):
        self.state = state


class City:
    state: str
    city: str

    def __init__(self, state: str, city: str):
        self.state = state
        self.city = city


class District:
    state: str
    city: str
    neighborhood: str

    def __init__(self, state: str, city: str, neighborhood: str):
        self.state = state
        self.city = city
        self.neighborhood = neighborhood


class AddressSearchService:
    def _get(self, type: str, kwargs: dict) -> List:
        # http get request to the address search service
        url = settings.CLOUD_FUNCTION_ADDRESS_SEARCH
        response = requests.get(url, params={"request_type": type, **kwargs})
        response.raise_for_status()
        return response.json()

    def get_city_districts(self, city: str, state: str) -> List[District]:
        districts = self._get("NEIGHBORHOODS_BY_CITY_AND_STATE", {
                              "city": city, "state": state})
        return [District(state=district["state"], city=district["city"], neighborhood=district["neighborhood"]) for district in districts]

    def get_cities(self, state: str) -> List[City]:
        cities = self._get("CITIES_BY_STATE", {"state": state})
        return [City(state=city["state"], city=city["city"]) for city in cities]

    def get_states(self) -> List[State]:
        states = self._get("STATES", {})
        return [State(state=state["state"]) for state in states]
