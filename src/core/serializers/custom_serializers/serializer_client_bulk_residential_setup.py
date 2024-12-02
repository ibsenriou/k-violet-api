from typing import List

from rest_framework import serializers

from src.condominium.models import Residential, Condominium, CondominiumGrouping
from src.lookups.models import LookupTypeOfCondominiumGrouping, LookupTypeOfResidential


class ClientBulkResidentialSetupSerializer(serializers.Serializer):
    """
    Receives the data from a Condominium, a LookupTypeOfCondominiumGrouping, a LookupTypeOfResidential and
    a list of Strings representing the names of the residential units to be created.
    """

    fk_condominium = serializers.UUIDField()
    fk_lookup_type_of_condominium_grouping = serializers.UUIDField()
    condominium_grouping_description = serializers.CharField(max_length=255, required=False)
    fk_lookup_type_of_residential = serializers.UUIDField()

    residential_units = serializers.CharField(max_length=10000)

    def create(self, validated_data):
        condominium_id = validated_data.get('fk_condominium')
        grouping_type_id = validated_data.get('fk_lookup_type_of_condominium_grouping')
        grouping_name = validated_data.get('condominium_grouping_description')
        residential_type_id = validated_data.get('fk_lookup_type_of_residential')
        residential_units = validated_data.get('residential_units')

        # Check existence of Condominium
        try:
            Condominium.objects.get(id=condominium_id)
        except Condominium.DoesNotExist:
            raise serializers.ValidationError(f"Condominium with ID {condominium_id} does not exist")

        # Check existence of Grouping Type
        try:
            LookupTypeOfCondominiumGrouping.objects.get(id=grouping_type_id)
        except LookupTypeOfCondominiumGrouping.DoesNotExist:
            raise serializers.ValidationError(
                f"LookupTypeOfCondominiumGrouping with ID {grouping_type_id} does not exist")

        # Check existence of Residential Type
        try:
            LookupTypeOfResidential.objects.get(id=residential_type_id)
        except LookupTypeOfResidential.DoesNotExist:
            raise serializers.ValidationError(f"LookupTypeOfResidential with ID {residential_type_id} does not exist")

        if grouping_name is not None:
            # Try to get the CondominiumGrouping or create it if it does not exist
            try:
                condominium_grouping, _ = CondominiumGrouping.objects.get_or_create(
                    name=grouping_name,
                    fk_uhab_id=condominium_id,
                    fk_lookup_type_of_condominium_grouping_id=grouping_type_id,
                    fk_condominium_id=condominium_id    
                )
            except Exception as e:
                raise serializers.ValidationError("Failed to create condominium grouping: " + str(e))
        else:
            # If no grouping name is provided, there's no grouping to create and the grouping is the Condominium itself
            condominium_grouping = Condominium.objects.get(
                id=condominium_id,
            )

        # Create Residential instances
        from django.db import transaction

        # Split the string of residential units into individual strings
        residential_unit_lists: List[str] = [unit.strip() for unit in residential_units.split(',')]

        try:
            with transaction.atomic():
                for unit in residential_unit_lists:
                    # Create a Residential instance for each residential unit string
                    Residential.objects.create(
                        fk_uhab=condominium_grouping,
                        fk_lookup_type_of_residential_id=residential_type_id,
                        name=unit,
                        fk_condominium_id=condominium_id
                    )
        except Exception as e:
            # Handle any errors during creation
            raise serializers.ValidationError("Failed to create residential units: " + str(e))