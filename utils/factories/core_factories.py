import datetime

from src.condominium.models import Uhab
from src.core.models import Color, Country, State, City, District, PostalCode, Address, Year, Period, Month, \
    MeasurementUnit, CustomUser
from src.people.models import Person
from utils.google.maps import Address as GoogleAddress
from utils.address_search.service import District as AddressSearchDistrict


class CoreFactory:
    """
        This class is a container for helper functions that create 'Core' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Core' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_color(description: str = 'Black') -> Color:
        cor, _ = Color.objects.get_or_create(description=description)
        return cor

    @staticmethod
    def create_country(
            country_name: str = 'Brasil',
            country_two_digits_code: str = 'BR',
            country_three_digits_code: str = 'BRA'
    ) -> Country:
        pais, _ = Country.objects.get_or_create(
            country_name=country_name,
            country_two_digits_code=country_two_digits_code,
            country_three_digits_code=country_three_digits_code
        )
        return pais

    @staticmethod
    def create_state(
            fk_country: Country | None = None,
            state_name: str = 'São Paulo',
            state_two_digits_code: str = 'SP'
    ) -> State:
        if not fk_country:
            fk_country = CoreFactory.create_country()

        state, _ = State.objects.get_or_create(
            fk_country=fk_country,
            state_name=state_name,
            state_two_digits_code=state_two_digits_code
        )

        return state

    @staticmethod
    def create_city(city_name: str = 'Campinas',
                    fk_state: State | None = None) -> City:

        if not fk_state:
            fk_state = CoreFactory.create_state()

        city, _ = City.objects.get_or_create(
            city_name=city_name, fk_state=fk_state)

        return city

    @staticmethod
    def create_district(district_name: str = 'Center',
                        fk_city: City | None = None) -> District:
        if not fk_city:
            fk_city = CoreFactory.create_city()

        district, _ = District.objects.get_or_create(
            district_name=district_name, fk_city=fk_city)
        return district

    @staticmethod
    def create_postal_code(postal_code_number: str = '13840000',
                           street_name: str = 'Rua 1',
                           fk_city: City | None = None,
                           fk_district: District | None = None,
                           ) -> PostalCode:
        if not fk_city:
            fk_city = CoreFactory.create_city()

        if not fk_district:
            fk_district = CoreFactory.create_district()

        postal_code, _ = PostalCode.objects.get_or_create(postal_code_number=postal_code_number,
                                                          street_name=street_name,
                                                          fk_city=fk_city,
                                                          fk_district=fk_district)
        return postal_code

    @staticmethod
    def create_address(
            fk_postal_code: PostalCode | None = None,
            fk_state: State | None = None,
            fk_city: City | None = None,
            fk_district: District | None = None,
            street_name: str = '',
            number: str = '1',
            complement: str = '',

            fk_uhab: Uhab | None = None,
            fk_person: Person | None = None) -> Address:

        if not fk_postal_code:
            fk_postal_code = CoreFactory.create_postal_code()

        if not fk_state:
            fk_state = CoreFactory.create_state()

        address = Address.objects.create(
            fk_postal_code=fk_postal_code,
            fk_state=fk_state,
            fk_city=fk_city,
            fk_district=fk_district,
            street_name=street_name,
            number=number,
            complement=complement,
            fk_uhab=fk_uhab,
            fk_person=fk_person
        )
        return address

    @staticmethod
    def create_year(year: str = '2023') -> Year:
        created_year, _ = Year.objects.get_or_create(year=year)

        return created_year

    @staticmethod
    def create_month(
            month_number: str = '01',
            month_description: str = 'Janeiro',
            month_three_chars_abbreviation: str = 'Jan'
    ) -> Month:
        month, _ = Month.objects.get_or_create(
            month_number=month_number,
            month_description=month_description,
            month_three_chars_abbreviation=month_three_chars_abbreviation
        )
        return month

    @staticmethod
    def create_period(
            period_code: str = '2023.01',
            start_date: datetime.date = datetime.date(2023, 1, 1),
            end_date: datetime.date = datetime.date(2023, 1, 31),

            fk_year: Year | None = None,
            fk_month: Month | None = None,
            fk_period_previous_period: Period | None = None,
            fk_period_next_period: Period | None = None
    ) -> Period:
        if not fk_year:
            fk_year = CoreFactory.create_year()

        if not fk_month:
            fk_month = CoreFactory.create_month()

        period, _ = Period.objects.get_or_create(
            period_code=period_code,
            start_date=start_date,
            end_date=end_date,

            fk_year=fk_year,
            fk_month=fk_month,
            fk_period_previous_period=fk_period_previous_period,
            fk_period_next_period=fk_period_next_period
        )
        return period

    @staticmethod
    def create_measurement_unit(
            
            character_abbreviation: str = 'KWH',
            description: str = 'KiloWatt'

    ) -> MeasurementUnit:

        measurement_unit, _ = MeasurementUnit.objects.get_or_create(
            
            character_abbreviation=character_abbreviation,
            description=description
        )

        return measurement_unit

    @staticmethod
    def create_custom_user(
            email: str = 'admin@admin.com',
            first_name: str = 'Admin',
            last_name: str = 'Admin',
            is_active: bool = True,
            is_staff: bool = True,
            is_superuser: bool = True,
            password: str = 'admin'
    ) -> CustomUser:
        custom_user, _ = CustomUser.objects.get_or_create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        custom_user.set_password(password)
        custom_user.save()

        return custom_user

    @staticmethod
    def create_google_address(postal_code: str = '13840000') -> GoogleAddress:
        return GoogleAddress(
            postal_code=postal_code,
            formatted_address='Rua Teste, 1 - Centro, Campinas - SP, 13010-000, Brasil',
            country='Brasil',
            country_code='BR',
            country_three_code='BRA',
            state='São Paulo',
            state_code='SP',
            city='Campinas',
            neighborhood='Centro',
            street='Rua Teste'
        )

    @staticmethod
    def create_google_address_without_street_and_district_info(postal_code: str = '13840000') -> GoogleAddress:
        return GoogleAddress(
            postal_code=postal_code,
            formatted_address='Campinas - SP, 13010-000, Brasil',
            country='Brasil',
            country_code='BR',
            country_three_code='BRA',
            state='São Paulo',
            state_code='SP',
            city='Campinas',
        )

    @staticmethod
    def create_address_search_districts() -> list[dict]:
        return [AddressSearchDistrict("SP", "Campinas", "Centro")]

    @staticmethod
    def create_all_colors() -> list[Color]:
        """
        Create all colors.
        """
        amarelo = CoreFactory.create_color('Amarelo')
        azul = CoreFactory.create_color('Azul')
        bege = CoreFactory.create_color('Bege')
        branco = CoreFactory.create_color('Branco')
        bronze = CoreFactory.create_color('Bronze')
        cinza = CoreFactory.create_color('Cinza')
        dourado = CoreFactory.create_color('Dourado')
        indefinida = CoreFactory.create_color('Indefinida')
        laranja = CoreFactory.create_color('Laranja')
        marrom = CoreFactory.create_color('Marrom')
        prata = CoreFactory.create_color('Prata')
        preto = CoreFactory.create_color('Preto')
        rosa = CoreFactory.create_color('Rosa')
        roxo = CoreFactory.create_color('Roxo')
        verde = CoreFactory.create_color('Verde')
        vermelho = CoreFactory.create_color('Vermelho')
        vinho = CoreFactory.create_color('Vinho')

        return [amarelo, azul, bege, branco, bronze, cinza, dourado, indefinida, laranja, marrom, prata, preto, rosa,
                roxo, verde, vermelho, vinho]

    def create_mesurerement_unit(description: str = 'm3') -> MeasurementUnit:
        mesurerement_unit, _ = MeasurementUnit.objects.get_or_create(
            description=description)
        return mesurerement_unit
