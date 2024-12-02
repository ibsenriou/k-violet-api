import datetime
import decimal
from typing import List

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from src.lookups.models import LookupTypeOfUhabUserRole, LookupTypeOfCondominiumGrouping

from src.condominium.models import (
    Uhab,
    CondominiumCommonArea,
    Condominium,
    CondominiumCommonAreaUtilizationFeeHistory,
    CondominiumCommonAreaItem,
    CondominiumGrouping,
    Residential,
    Commercial,
    Garage,
    UhabUserRole,
    CondominiumContactInformation,
    CondominiumCommonAreaReservationPeriod,
    CondominiumCommonAreaReservation,
    CondominiumCommonAreaArchiveOfRules,
    ReadingItem
)

from src.core.models import Address
from src.people.models import Person
from src.people.models import NaturalPerson
from src.lookups.models import LookupTypeOfContactInformation
from src.lookups.models import LookupTypeOfResidential
from src.lookups.models import LookupTypeOfCommercial

from utils.factories.auth_factories import AuthFactory
from utils.factories.core_factories import CoreFactory
from utils.factories.people_factories import PeopleFactory, LookupFactory


class CondominiumFactory:
    """
        This class is a container for helper functions that create 'Condominium' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Condominium' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_uhab(
            name: str = 'Uhab',
            description: str = 'Uhab description') -> Uhab:

        uhab, created = Uhab.objects.get_or_create(name=name, description=description)
        return uhab

    @staticmethod
    def create_condominium(
            name: str = "Condominio Pedra Rubi",
            description: str = "Description for Condominio Pedra Rubi",
            national_corporate_taxpayer_identification_number: str = '12345678901234',
            fk_address: Address | None = None) -> Condominium:

        if not fk_address:
            fk_address = CoreFactory.create_address()

        condominium, _ = Condominium.objects.get_or_create(
            name=name,
            description=description,
            national_corporate_taxpayer_identification_number=national_corporate_taxpayer_identification_number,
            fk_address=fk_address,
        )

        return condominium

    @staticmethod
    def create_condominium_contact_information(
            fk_lookup_type_of_contact_information: LookupTypeOfContactInformation | None = None,
            contact: str = '11999999999',
            description: str = 'Contato de Condomínio 1',
            fk_condominium: Condominium | None = None
    ) -> CondominiumContactInformation:

        if not fk_lookup_type_of_contact_information:
            fk_lookup_type_of_contact_information = LookupFactory.create_lookup_type_of_contact_information()

        if not fk_condominium:
            fk_condominium = CondominiumFactory.create_condominium()

        return CondominiumContactInformation.objects.create(
            fk_lookup_type_of_contact_information=fk_lookup_type_of_contact_information,
            contact=contact,
            description=description,
            fk_condominium=fk_condominium
        )

    @staticmethod
    def create_condominium_grouping(
            name: str = 'Grouping 1',
            description: str = 'Block',
            fk_uhab: Uhab | None = None,
            fk_lookup_type_of_condominium_grouping: LookupTypeOfCondominiumGrouping | None = None,
            fk_condominium_id: str | None = None
    ) -> CondominiumGrouping:

        if not fk_lookup_type_of_condominium_grouping:
            fk_lookup_type_of_condominium_grouping, _ = LookupTypeOfCondominiumGrouping.objects.get_or_create(
                description='Block')

        condominium_grouping, _ = CondominiumGrouping.objects.get_or_create(
            name=name,
            description=description,
            fk_uhab=fk_uhab,
            fk_lookup_type_of_condominium_grouping=fk_lookup_type_of_condominium_grouping,
            fk_condominium_id=fk_condominium_id
        )

        return condominium_grouping

    @staticmethod
    def create_residential(name: str = 'Residencial 1',
                           description: str = 'Descrição do Residencial 1',
                           fk_uhab: Uhab | None = None,
                           fk_lookup_type_of_residential: LookupTypeOfResidential | None = None,
                           ) -> Residential:

        if not fk_lookup_type_of_residential:
            fk_lookup_type_of_residential = LookupFactory.create_lookup_type_of_residential()

        return Residential.objects.create(
            name=name,
            description=description,
            fk_uhab=fk_uhab,
            fk_lookup_type_of_residential=fk_lookup_type_of_residential,
        )

    @staticmethod
    def create_commercial(name: str = 'Commercial 1',
                          description: str = 'Descrição do Comercial 1',
                          fk_uhab: Uhab | None = None,
                          fk_lookup_type_of_commercial: LookupTypeOfCommercial | None = None,
                          ) -> Commercial:

        if not fk_lookup_type_of_commercial:
            fk_lookup_type_of_commercial = LookupFactory.create_lookup_type_of_commercial()

        return Commercial.objects.create(
            name=name,
            description=description,
            fk_uhab=fk_uhab,
            fk_lookup_type_of_commercial=fk_lookup_type_of_commercial,
        )

    @staticmethod
    def create_condominium_common_area(
            name: str = 'Área Comum 01',
            description: str = 'Descrição de Área Comum 01',
            fk_uhab: Uhab | None = None,
            capacity_of_people: int = 100,
            does_it_requires_reservation: bool = True,
            does_it_allows_guests: bool = True,
            does_it_have_usage_fee: bool = True,
            does_it_allows_reservation_to_defaulters: bool = True,
            does_it_have_entry_checklist: bool = True,
            does_it_have_exit_checklist: bool = True,
            fk_condominium_common_area_utilization_fee_history: CondominiumCommonAreaUtilizationFeeHistory | None = None

    ) -> CondominiumCommonArea:

        return CondominiumCommonArea.objects.create(
            name=name,
            description=description,
            fk_uhab=fk_uhab,
            does_it_requires_reservation=does_it_requires_reservation,
            does_it_have_usage_fee=does_it_have_usage_fee,
            fk_condominium_common_area_utilization_fee_history=fk_condominium_common_area_utilization_fee_history,
            does_it_allows_reservation_to_defaulters=does_it_allows_reservation_to_defaulters,
            does_it_have_entry_checklist=does_it_have_entry_checklist,
            does_it_have_exit_checklist=does_it_have_exit_checklist,
            does_it_allows_guests=does_it_allows_guests,
            capacity_of_people=capacity_of_people,
        )

    @staticmethod
    def create_condominium_common_area_item(fk_condominium_common_area: CondominiumCommonArea = None,
                                            description: str = 'Playstation 5',
                                            quantity_of_items: int = 1,
                                            unitary_value: float = 5000.00,
                                            item_model: str = '',
                                            item_brand: str = '',
                                            date_of_acquisition: datetime.date | None = None,
                                            observations: str = ''
                                            ) -> CondominiumCommonAreaItem:

        if not fk_condominium_common_area:
            fk_condominium_common_area = CondominiumFactory.create_condominium_common_area()

        return CondominiumCommonAreaItem.objects.create(
            fk_condominium_common_area=fk_condominium_common_area,
            description=description,
            quantity_of_items=quantity_of_items,
            unitary_value=unitary_value,
            item_model=item_model,
            item_brand=item_brand,
            date_of_acquisition=date_of_acquisition,
            observations=observations
        )

    @staticmethod
    def create_condominium_common_area_reservation_period(
            fk_condominium_common_area: CondominiumCommonArea | None = None,
            is_full_day: bool = False,
            start_time: datetime.time = datetime.time(8, 0, 0),
            end_time: datetime.time = datetime.time(18, 0, 0),
            is_period_active: bool = True
    ) -> CondominiumCommonAreaReservationPeriod:

        if not fk_condominium_common_area:
            fk_condominium_common_area = CondominiumFactory.create_condominium_common_area()

        return CondominiumCommonAreaReservationPeriod.objects.create(
            fk_condominium_common_area=fk_condominium_common_area,
            is_full_day=is_full_day,
            start_time=start_time,
            end_time=end_time,
            is_period_active=is_period_active
        )

    @staticmethod
    def create_condominium_common_area_archive_of_rules(
            description: str = 'Main Rule',
            is_rule_active: bool = True,
            file_of_rules_attachment: SimpleUploadedFile = None,
            fk_condominium_common_area: CondominiumCommonArea = None,
            created_by: User | None = None,
            created_at: datetime.date = datetime.date.today()
    ) -> CondominiumCommonAreaArchiveOfRules:

        if not fk_condominium_common_area:
            fk_condominium_common_area = CondominiumFactory.create_condominium_common_area()

        if not created_by:
            created_by = AuthFactory.create_user()

        if not file_of_rules_attachment:
            file_of_rules_attachment = SimpleUploadedFile(
                "simple_text_file.txt",
                b"these are the file contents!"
            )

        return CondominiumCommonAreaArchiveOfRules.objects.create(
            description=description,
            is_rule_active=is_rule_active,
            file_of_rules_attachment=file_of_rules_attachment,
            fk_condominium_common_area=fk_condominium_common_area,
            created_by=created_by,
            created_at=created_at
        )

    @staticmethod
    def create_garage(name: str = 'Garagem 1',
                      description: str = 'Descrição da Garagem 1',
                      fk_uhab: Uhab | None = None,
                      number_of_spots: int = 1,
                      is_garage_being_used: bool = True,
                      is_garage_available_for_rent: bool = False,
                      is_drawer_type_garage: bool = False,
                      is_covered_type_garage: bool = False) -> Garage:

        return Garage.objects.create(
            name=name,
            description=description,
            fk_uhab=fk_uhab,
            number_of_spots=number_of_spots,
            is_garage_being_used=is_garage_being_used,
            is_garage_available_for_rent=is_garage_available_for_rent,
            is_drawer_type_garage=is_drawer_type_garage,
            is_covered_type_garage=is_covered_type_garage
        )

    @staticmethod
    def create_uhab_user_role(fk_person: Person = None,
                              fk_uhab: Uhab | None = None,
                              fk_lookup_type_of_uhab_user_role: LookupTypeOfUhabUserRole = None,
                              fk_condominium: Condominium | None = None,
                              is_this_the_main_role: bool = True,
                              deactivated_at: datetime.datetime | None = None) -> UhabUserRole:

        if not fk_person:
            fk_person = PeopleFactory.create_person()

        if not fk_uhab:
            fk_uhab = CondominiumFactory.create_uhab()

        if not fk_lookup_type_of_uhab_user_role:
            fk_lookup_type_of_uhab_user_role = LookupFactory.create_lookup_type_of_uhab_user_role()

        if not fk_condominium:
            fk_condominium = CondominiumFactory.create_condominium()

        uhab_user_role, _ = UhabUserRole.objects.get_or_create(
            fk_person=fk_person,
            fk_lookup_type_of_uhab_user_role=fk_lookup_type_of_uhab_user_role,
            fk_uhab=fk_uhab,
            fk_condominium=fk_condominium,
            is_this_the_main_role=is_this_the_main_role,
            deactivated_at=deactivated_at,
        )

        return uhab_user_role

    @staticmethod
    def create_condominium_common_area_reservation(
            fk_condominium_common_area: CondominiumCommonArea | None = None,
            fk_person_as_reservant: Person | None = None,
            fk_uhab_as_reservant: Residential | None = None,
            reservation_date: datetime.date = datetime.date.today(),
            fk_common_area_reservation_period: CondominiumCommonAreaReservationPeriod | None = None,
            simple_guest_list: str = '',
            fks_natural_person_complete_guest_list: List[NaturalPerson] | None = None,
            is_reservation_approved_by_syndicator: bool = False,
            is_this_a_blockation_reservation: bool = False,
    ) -> CondominiumCommonAreaReservation:

        if not fk_condominium_common_area:
            fk_condominium_common_area = CondominiumFactory.create_condominium_common_area()

        if not fk_person_as_reservant:
            fk_person_as_reservant = PeopleFactory.create_natural_person()

        if not fk_common_area_reservation_period:
            fk_common_area_reservation_period = CondominiumFactory.create_condominium_common_area_reservation_period()

        condominium_common_area_reservation = CondominiumCommonAreaReservation.objects.create(
            fk_condominium_common_area=fk_condominium_common_area,
            fk_person_as_reservant=fk_person_as_reservant,
            fk_uhab_as_reservant=fk_uhab_as_reservant,
            reservation_date=reservation_date,
            fk_common_area_reservation_period=fk_common_area_reservation_period,
            simple_guest_list=simple_guest_list,
            is_reservation_approved_by_syndicator=is_reservation_approved_by_syndicator,
            is_this_a_blockation_reservation=is_this_a_blockation_reservation,
        )

        if fks_natural_person_complete_guest_list:
            condominium_common_area_reservation.fks_natural_person_complete_guest_list.set(
                fks_natural_person_complete_guest_list)

        return condominium_common_area_reservation

    @staticmethod
    def create_condominium_common_area_utilization_fee_history(
            fk_common_area: CondominiumCommonArea | None = None,
            date_since_its_valid: datetime.date = datetime.date.today(),
            value: decimal = 100.50,
            created_at: datetime.date = datetime.date.today(),
            created_by: User | None = None
    ) -> CondominiumCommonAreaUtilizationFeeHistory:

        if not fk_common_area:
            fk_common_area = CondominiumFactory.create_condominium_common_area()

        if not created_by:
            created_by = AuthFactory.create_user()

        return CondominiumCommonAreaUtilizationFeeHistory.objects.create(
            fk_common_area=fk_common_area,
            date_since_its_valid=date_since_its_valid,
            value=value,
            created_at=created_at,
            created_by=created_by
        )
    

    def create_reading_item(
        fk_measurement_unit: ReadingItem | None = None,
        description = 'Luz',            
        fk_condominium: Condominium | None = None
    ) -> ReadingItem:

        if not fk_measurement_unit:
            fk_measurement_unit = CoreFactory.create_measurement_unit()

        if not fk_condominium:
            fk_condominium = CondominiumFactory.create_condominium()

        return ReadingItem.objects.create(
            fk_measurement_unit = fk_measurement_unit,
            description = description,            
            fk_condominium=fk_condominium
        )