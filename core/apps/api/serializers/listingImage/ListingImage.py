from rest_framework import serializers

from core.apps.api.models import ListingimageModel


class BaseListingimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingimageModel
        fields = [
            "id",
            "name",
        ]


class ListListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta): ...


class RetrieveListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta): ...


class CreateListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
