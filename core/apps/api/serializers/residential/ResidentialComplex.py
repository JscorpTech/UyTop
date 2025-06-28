from rest_framework import serializers

from core.apps.api.models import ResidentialcomplexModel


class BaseResidentialcomplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialcomplexModel
        fields = [
            "id",
            "name",
        ]


class ListResidentialcomplexSerializer(BaseResidentialcomplexSerializer):
    class Meta(BaseResidentialcomplexSerializer.Meta): ...


class RetrieveResidentialcomplexSerializer(BaseResidentialcomplexSerializer):
    class Meta(BaseResidentialcomplexSerializer.Meta): ...


class CreateResidentialcomplexSerializer(BaseResidentialcomplexSerializer):
    class Meta(BaseResidentialcomplexSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
