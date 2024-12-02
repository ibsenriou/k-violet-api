import datetime
from typing import Optional, List

from django.contrib.auth import get_user_model

from src.core.models.model_address import Address
from src.people.models import PersonContactInformation
from src.people.models import Person, NaturalPerson, LegalPerson, Employee

from src.lookups.models import LookupTypeOfContactInformation

from utils.factories.lookup_factories import LookupFactory


class PeopleFactory:
    """
        This class is a container for helper functions that create 'Pessoas' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Pessoas' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_person(name: str = 'Person 1',
                      fks_address: List[Address] = None,
                      fk_user: Optional[get_user_model()] = None,
                      ) -> Person:
        person = Person.objects.create(
            name=name,
            fk_user=fk_user,
        )

        if fks_address is not None:
            person.fks_address.set(fks_address)

        return person

    @staticmethod
    def create_natural_person(
        name: str = 'John Doe',
        national_individual_taxpayer_identification: str = '12345678901',
        date_of_birth: datetime.datetime = datetime.datetime(1990, 1, 1),
        has_natural_person_given_permission_to_use_his_image: bool = False,
        avatar_image_file_name: str = 'avatar-01.png',
        fks_address: List[Address] = None,
    ) -> NaturalPerson:

        natural_person, _ = NaturalPerson.objects.get_or_create(
            name=name,
            national_individual_taxpayer_identification=national_individual_taxpayer_identification,
            date_of_birth=date_of_birth,
            has_natural_person_given_permission_to_use_his_image=has_natural_person_given_permission_to_use_his_image,
            avatar_image_file_name=avatar_image_file_name
        )

        if fks_address is not None:
            natural_person.fks_address.set(fks_address)

        return natural_person

    @staticmethod
    def create_legal_person(
            name: str = 'Company John Doe',
            national_corporate_taxpayer_identification_number: str = '12345678901234',
            fks_address: List[Address] = None,
    ) -> LegalPerson:

        legal_person, _ = LegalPerson.objects.get_or_create(
            name=name,
            national_corporate_taxpayer_identification_number=national_corporate_taxpayer_identification_number,
        )

        if fks_address is not None:
            legal_person.fks_address.set(fks_address)

        return legal_person

    @staticmethod
    def create_employee(name: str = 'John Doe Employer',
                        national_individual_taxpayer_identification: str = '12345678901',
                        date_of_birth: datetime.datetime = datetime.datetime(1990, 1, 1),
                        has_natural_person_given_permission_to_use_his_image: bool = False,
                        avatar_image_file_name: str = 'avatar-01.png',
                        fks_address: List[Address] = None,
                        ) -> Employee:

        employee, _ = Employee.objects.get_or_create(
            name=name,
            national_individual_taxpayer_identification=national_individual_taxpayer_identification,
            date_of_birth=date_of_birth,
            has_natural_person_given_permission_to_use_his_image=has_natural_person_given_permission_to_use_his_image,
            avatar_image_file_name=avatar_image_file_name,
        )

        if fks_address is not None:
            employee.fks_address.set(fks_address)

        return employee

    @staticmethod
    def create_person_contact_information(
            description: str = 'email@email.com',
            fk_lookup_type_of_contact_information: LookupTypeOfContactInformation | None = None,
            fk_person: Person | None = None
    ) -> PersonContactInformation:
        if fk_lookup_type_of_contact_information is None:
            fk_lookup_type_of_contact_information = LookupFactory.create_lookup_type_of_contact_information()

        if fk_person is None:
            fk_person = PeopleFactory.create_person()

        return PersonContactInformation.objects.create(
            description=description,
            fk_lookup_type_of_contact_information=fk_lookup_type_of_contact_information,
            fk_person=fk_person
        )
