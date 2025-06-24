from rest_framework import serializers

from core.apps.api.models import AmenityModel


class BaseAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityModel
        fields = [
            "id",
            "name",
        ]


class ListAmenitySerializer(BaseAmenitySerializer):
    class Meta(BaseAmenitySerializer.Meta): ...


class RetrieveAmenitySerializer(BaseAmenitySerializer):
    class Meta(BaseAmenitySerializer.Meta): ...


class CreateAmenitySerializer(BaseAmenitySerializer):
    class Meta(BaseAmenitySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
