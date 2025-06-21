from rest_framework import serializers

from core.apps.api.models import PropertysubtypeModel


class BasePropertysubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertysubtypeModel
        fields = [
            "id",
            "name",
        ]


class ListPropertysubtypeSerializer(BaseListingsubtypeSerializer):
    class Meta(BasePropertysubtypeSerializer.Meta): ...


class RetrievePropertysubtypeSerializer(BasePropertysubtypeSerializer):
    class Meta(BasePropertysubtypeSerializer.Meta): ...


class CreatePropertysubtypeSerializer(BasePropertysubtypeSerializer):
    class Meta(BasePropertysubtypeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
