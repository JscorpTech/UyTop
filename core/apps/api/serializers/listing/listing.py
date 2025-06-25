from rest_framework import serializers

from core.apps.api.models import ListingModel


class BaseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields = [
            "id",
            "name",
            "dealtype",
            "property",
            "latitude",
            "longitude",
            "room_count",
            "area",
            "floor",
            "total_floors",
            "repair_type",
            "building",
            "price_type",
            "price",
            "currency",
            "description",
            "amenity",
            "phone"
            
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
            "dealtype",
            "property",
            "latitude",
            "longitude",
            "room_count",
            "area",
            "floor",
            "total_floors",
            "repair_type",
            "building",
            "price_type",
            "price",
            "currency",
            "description",
            "amenity",
            "phone"
        ]
