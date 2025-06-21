from rest_framework import serializers

from core.apps.api.models import ListingModel


class BaseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields = [
            "id",
            "name",
        ]


class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class RetrieveListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class CreateListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
