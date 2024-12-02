from src.lookups.models import (
    LookupTypeOfUhabUserRole,
    LookupTypeOfContactInformation,
    LookupTypeOfResidential,
    LookupTypeOfCommercial,
    LookupTypeOfCondominiumGrouping, LookupTypeOfPaymentForm,
)
from src.lookups.models.model_lookup_type_of_bank_account import LookupTypeOfBankAccount


class LookupFactory:
    """
        This class is a container for helper functions that create 'Lookup' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Lookup' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_lookup_type_of_condominium_grouping(description: str = 'Block') -> LookupTypeOfCondominiumGrouping:
        lookup_type_of_condominium_grouping, _ = LookupTypeOfCondominiumGrouping.objects.get_or_create(
            description=description)
        return lookup_type_of_condominium_grouping

    @staticmethod
    def create_lookup_type_of_residential(description: str = 'Apartment') -> LookupTypeOfResidential:
        lookup_type_of_residential, _ = LookupTypeOfResidential.objects.get_or_create(
            description=description)

        return lookup_type_of_residential

    @staticmethod
    def create_lookup_type_of_commercial(description: str = 'Commercial room') -> LookupTypeOfCommercial:
        lookup_type_of_commercial, _ = LookupTypeOfCommercial.objects.get_or_create(
            description=description)

        return lookup_type_of_commercial

    @staticmethod
    def create_lookup_type_of_contact_information(description: str = 'E-mail') -> LookupTypeOfContactInformation:
        lookup_type_of_contact_information, _ = LookupTypeOfContactInformation.objects.get_or_create(
            description=description)
        return lookup_type_of_contact_information

    @staticmethod
    def create_lookup_type_of_uhab_user_role(description: str = 'Resident, Commercial',
                                             name: str = 'Resident') -> LookupTypeOfUhabUserRole:

        lookup_type_of_uhab_user_role, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description=description,
        )

        return lookup_type_of_uhab_user_role

    @staticmethod
    def create_lookup_type_of_contact_information_all() -> str:
        """
        Create lookup type of contact information.
        """
        email = LookupFactory.create_lookup_type_of_contact_information(
            description='E-mail')
        telefone_celular = LookupFactory.create_lookup_type_of_contact_information(
            description='Telefone Celular')
        telefone_residencial = LookupFactory.create_lookup_type_of_contact_information(
            description='Telefone Residencial')
        telefone_comercial = LookupFactory.create_lookup_type_of_contact_information(
            description='Telefone Comercial')

        return [email, telefone_celular, telefone_residencial, telefone_comercial]

    @staticmethod
    def create_lookup_types_of_uhab_user_role() -> str:
        """
        Create lookup types of uhab user role.
        """

        proprietary, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description='Proprietary',
        )

        syndicator, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description='Syndicator',
        )

        resident, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description='Resident',
        )
        renters, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description='Renters',
        )

        employee, _ = LookupTypeOfUhabUserRole.objects.get_or_create(
            description='Employee',
        )

        return [proprietary, syndicator, resident, renters, employee]

    @staticmethod
    def create_lookup_type_of_condominium_grouping_all() -> str:

        bloco = LookupFactory.create_lookup_type_of_condominium_grouping(
            description="Bloco")
        torre = LookupFactory.create_lookup_type_of_condominium_grouping(
            description="Torre")
        casa = LookupFactory.create_lookup_type_of_condominium_grouping(
            description="Casa")
        lote = LookupFactory.create_lookup_type_of_condominium_grouping(
            description="Lote")

        return [bloco, torre, casa, lote]

    @staticmethod
    def create_lookup_type_of_residential_all() -> str:
        """
        Create lookup type of residential.
        """
        apartamento = LookupFactory.create_lookup_type_of_residential(
            description='Apartamento')
        casa = LookupFactory.create_lookup_type_of_residential(
            description='Casa')
        kitnet = LookupFactory.create_lookup_type_of_residential(
            description='kitnet')
        lote = LookupFactory.create_lookup_type_of_residential(
            description='Lote')

        return [apartamento, casa, kitnet, lote]

    @staticmethod
    def create_lookup_type_of_commercial_all() -> str:
        """
        Create lookup type of commercial.
        """
        apartamento = LookupFactory.create_lookup_type_of_commercial(
            description='Apartamento')
        casa = LookupFactory.create_lookup_type_of_commercial(
            description='Casa')
        kitnet = LookupFactory.create_lookup_type_of_commercial(
            description='kitnet')
        lote = LookupFactory.create_lookup_type_of_commercial(
            description='Lote')

        return [apartamento, casa, kitnet, lote]

    @staticmethod
    def create_lookup_type_of_bank_account(description: str = 'Savings') -> LookupTypeOfBankAccount:
        lookup_type_of_bank_account, _ = LookupTypeOfBankAccount.objects.get_or_create(description=description)

        return lookup_type_of_bank_account

    @staticmethod
    def create_lookup_type_of_payment_form(description: str = 'Credit Card') -> LookupTypeOfPaymentForm:
        lookup_type_of_payment_form, _ = LookupTypeOfPaymentForm.objects.get_or_create(description=description)

        return lookup_type_of_payment_form
