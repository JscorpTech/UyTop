from rest_framework import serializers

from core.apps.api.models import ListingsubtypeModel


class BaseListingsubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingsubtypeModel
        fields = [
            "id",
            "name",
        ]


class ListListingsubtypeSerializer(BaseListingsubtypeSerializer):
    class Meta(BaseListingsubtypeSerializer.Meta): ...


class RetrieveListingsubtypeSerializer(BaseListingsubtypeSerializer):
    class Meta(BaseListingsubtypeSerializer.Meta): ...


class CreateListingsubtypeSerializer(BaseListingsubtypeSerializer):
    class Meta(BaseListingsubtypeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
