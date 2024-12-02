from django.conf import settings
import googlemaps

COUNTRY_NORMALIZATION = {
    "Brazil": "Brasil",
}

COUNTRY_THREE_CODE = {
    "BR": "BRA",
}


class Address:
    postal_code: str
    formatted_address: str
    country: str
    country_code: str
    country_three_code: str
    state: str
    state_code: str
    city: str
    neighborhood: str or None
    street: str or None

    def __init__(
        self,
            postal_code: str = "",
            formatted_address: str = "",
            country: str = "",
            country_code: str = "",
            country_three_code: str = "",
            state: str = "",
            state_code: str = "",
            city: str = "",
            neighborhood: str or None = None,
            street: str or None = None
    ):
        self.postal_code = postal_code
        self.formatted_address = formatted_address
        self.country = country
        self.country_code = country_code
        self.country_three_code = country_three_code
        self.state = state
        self.state_code = state_code
        self.city = city
        self.neighborhood = neighborhood
        self.street = street

    @staticmethod
    def from_geocode_result(geocode_result):
        address = Address()
        address.postal_code = Address.find_geocode_component_name(
            geocode_result, 'postal_code').replace('-', '')
        address.formatted_address = geocode_result['formatted_address']
        country = Address.find_geocode_component_name(
            geocode_result, 'country')
        address.country = COUNTRY_NORMALIZATION.get(country, country)
        address.country_code = Address.find_geocode_component_name(
            geocode_result, 'country', 'short_name')
        address.country_three_code = COUNTRY_THREE_CODE.get(
            address.country_code)
        address.state = Address.find_geocode_component_name(
            geocode_result, 'administrative_area_level_1').replace('State of ', '')
        address.state_code = Address.find_geocode_component_name(
            geocode_result, 'administrative_area_level_1', 'short_name')
        address.city = Address.find_geocode_component_name(
            geocode_result, 'administrative_area_level_2')
        address.neighborhood = Address.find_geocode_component_name(
            geocode_result, 'sublocality_level_1')
        address.street = Address.find_geocode_component_name(
            geocode_result, 'route')
        return address

    @staticmethod
    def find_geocode_component_name(geocode_result, component_type, name_type='long_name') -> str or None:
        for component in geocode_result['address_components']:
            if component_type in component['types']:
                return component[name_type]
        return None


class MapService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def get_address(self, address: str):
        geocode_result = self.client.geocode(address)
        if geocode_result is None:
            raise PostalCodeNotFound()
        if len(geocode_result) == 0:
            raise PostalCodeNotFound()

        return Address.from_geocode_result(geocode_result[0])


class PostalCodeNotFound(Exception):
    pass
