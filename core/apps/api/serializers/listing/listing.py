from rest_framework import serializers

from core.apps.api.models import ListingModel, ListingimageModel, AmenityModel
from core.apps.api.serializers.listingImage import BaseListingimageSerializer
from ...enums.Services import ListingServices as LS
from .currency import CurrencyPriceMixin




class BaseListingSerializer(CurrencyPriceMixin, serializers.ModelSerializer):
    property = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    
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
            "phone",
            "images"
        ]

    def get_property(self, obj):
        return LS.get_property(obj)
        
    def get_images(self, obj):
        request = self.context.get("request")
        return LS.get_images(obj, request)
    
    def get_amenity(self, obj):
        return LS.get_amenity(obj)
    

class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class RetrieveListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class CreateListingSerializer(serializers.ModelSerializer):
    images = BaseListingimageSerializer(many=True, write_only=True, required=False)
    amenity = serializers.PrimaryKeyRelatedField(
        queryset=AmenityModel.objects.all(),
        many=True,
        required=False
    )
    
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
            "price_uzs",
            "price_shb",
            "currency",
            "description",
            "amenity",
            "phone",
            "images"
        ]
        
    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        amenities = validated_data.pop("amenity", [])

        listing = ListingModel.objects.create(**validated_data)
        listing.amenity.set([a.id for a in amenities])  

        for image_data in images_data:
            ListingimageModel.objects.create(listing=listing, **image_data)

        return listing
