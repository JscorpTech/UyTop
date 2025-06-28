from rest_framework import serializers

from core.apps.api.models import ListingModel, ListingimageModel, AmenityModel
from core.apps.api.serializers.listingImage import BaseListingimageSerializer
from ...enums.Services import ListingServices as LS
from .currency import CurrencyPriceMixin





class BaseListingSerializer(serializers.ModelSerializer):
    building = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    residential_complex = serializers.SerializerMethodField()

    class Meta:
        model = ListingModel
        fields = [
            "id",
            "images",
            "price",
            "price_type",
            "room_count",
            "total_floors",
            "description",
            "residential_complex"
        ]

    def get_building(self, obj):
        return LS.get_building(obj)

    def get_images(self, obj):
        request = self.context.get("request")
        return LS.get_images(obj, request)
    
    
    def get_residential_complex(self, obj):
        return LS.get_residential_complex(obj)


    def get_amenity(self, obj):
        return LS.get_amenity(obj)


class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = BaseListingSerializer.Meta.fields + ["name", "dealtype"]


class RetrieveListingSerializer(CurrencyPriceMixin, serializers.ModelSerializer):
    building = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    residential_complex = serializers.SerializerMethodField()
    

    class Meta:
        model = ListingModel
        fields = [
            "id",
            "name",
            "dealtype",
            "property",
            "property_subtype",
            "latitude",
            "longitude",
            "address",
            "room_count",
            "floor",
            "total_floors",
            "floors_count",
            "apartment_area",
            "house_area",
            "land_area",
            "office_area",
            "building_area",
            "construction_area",
            "room_area",
            "repair_type",
            "building",
            "price_type",
            "price",
            "negotiable",
            "description",
            "phone",
            "residential_complex",
            "images",
            "amenity"
        ]

    def get_building(self, obj):
        return LS.get_building(obj)

    def get_images(self, obj):
        request = self.context.get("request")
        return LS.get_images(obj, request)

    def get_residential_complex(self, obj):
        return LS.get_residential_complex(obj)

    def get_amenity(self, obj):
        return LS.get_amenity(obj)




import json  # stringni listga aylantirish uchun

class CreateListingSerializer(serializers.ModelSerializer):
    images = BaseListingimageSerializer(many=True, write_only=True, required=False)
    
    # amenity ni oddiy string sifatida qabul qilamiz
    amenity = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = ListingModel
        fields = [
            "id",
            "name",
            "dealtype",
            "property",
            "property_subtype",
            "latitude",
            "longitude",
            "address",
            "room_count",
            "floor",
            "total_floors",
            "floors_count",
            "apartment_area",
            "house_area",
            "land_area",
            "office_area",
            "building_area",
            "construction_area",
            "room_area",
            "repair_type",
            "building",
            "price_type",
            "price",
            "negotiable",
            "description",
            "residential_complex",
            "phone",
            "amenity",
            "images"
        ]

    def validate_amenity(self, value):
        """
        amenity: '[4, 5]' yoki '["4", "5"]' => listga aylantiramiz
        """
        try:
            amenity_list = json.loads(value)  # stringdan list yasaymiz
            return [int(a) for a in amenity_list]
        except Exception:
            raise serializers.ValidationError("amenity must be a JSON list of IDs")

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        amenity_ids = validated_data.pop("amenity", [])

        listing = ListingModel.objects.create(**validated_data)

        amenities = AmenityModel.objects.filter(id__in=amenity_ids)
        listing.amenity.set(amenities)

        for image_data in images_data:
            ListingimageModel.objects.create(listing=listing, **image_data)

        return listing
