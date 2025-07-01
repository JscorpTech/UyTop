from rest_framework import serializers

from core.apps.api.models import ListingModel, ListingimageModel, AmenityModel
from ...enums.Services import ListingServices as LS
from .currency import CurrencyPriceMixin
from core.apps.api.models.favorite import FavoriteModel
import json  
from core.apps.accounts.serializers import UserSerializer




class BaseListingSerializer(serializers.ModelSerializer):
    building = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    residential_complex = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = ListingModel
        fields = [
            "id",
            "user",
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
            "currency",
            "residential_complex",
            "images",
            "amenity",
            "is_favorited"
        ]


    def get_is_favorited(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return FavoriteModel.objects.filter(user=request.user, listing=obj).exists()

    def get_user(self, obj):
        return UserSerializer(obj.user).data

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
            "currency",
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





class CreateListingSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
            child=serializers.ImageField(),
            write_only=True,
            required=False
    )    
    amenity = serializers.CharField(write_only=True, required=False)
    

    class Meta:
        model = ListingModel
        fields = [
            "id",
            "user",
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
            "currency",
            "amenity",
            "images"
        ]

        read_only_fields = ["user"]  
        
    def validate_amenity(self, value):
        try:
            amenity_list = json.loads(value)  
            return [int(a) for a in amenity_list]
        except Exception:
            raise serializers.ValidationError("amenity must be a JSON list of IDs")


    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        
        if not user:
            raise serializers.ValidationError("foydalanuvchi yoq dedimku")
        
        images = validated_data.pop("images", [])
        amenity_ids = validated_data.pop("amenity", [])

        validated_data["user"] = user

        listing = ListingModel.objects.create(**validated_data)

        if amenity_ids:
            amenities = AmenityModel.objects.filter(id__in=amenity_ids)
            listing.amenity.set(amenities)

        for image in images:
            ListingimageModel.objects.create(listing=listing, image=image)

        return listing