from rest_framework import serializers
from core.apps.api.models import ListingimageModel


class BaseListingimageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ListingimageModel
        fields = [
            "id",
            "listing",
            "image"
        ]
        read_only_fields = ["id", "listing"]  


class ListListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta):
        pass


class RetrieveListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta):
        pass


class CreateListingimageSerializer(BaseListingimageSerializer):
    class Meta(BaseListingimageSerializer.Meta):
        fields = [
            "id",
            "listing",
            "image"
        ]
        read_only_fields = ["id", "listing"]
