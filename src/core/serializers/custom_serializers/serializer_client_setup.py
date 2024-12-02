from rest_framework import serializers


class ClientSetupSerializer(serializers.Serializer):
    """Client setup serializer."""

    client_first_name = serializers.CharField(max_length=255)
    client_last_name = serializers.CharField(max_length=255)
    client_date_of_birth = serializers.DateField()
    client_national_individual_taxpayer_identification = serializers.CharField(max_length=11)
    client_email = serializers.EmailField()

    condominium_name = serializers.CharField(max_length=255)
    condominium_national_corporate_taxpayer_identification_number = serializers.CharField(max_length=14)
    postal_code_id = serializers.CharField(max_length=255)
    condominium_address_street_number = serializers.CharField(max_length=255)
