from rest_framework import serializers

from core.apps.api.models import ListingModel, ListingimageModel, AmenityModel, ToplistingpriceModel
from ...enums.Services import ListingServices as LS
from .currency import CurrencyPriceMixin
from core.apps.api.models.favorite import FavoriteModel
import json  
from core.apps.accounts.serializers import UserSerializer
from .enums.send_telegram import send_telegram




class BaseListingSerializer(serializers.ModelSerializer):
    building = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    residential_complex = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()
    toplisting = serializers.SerializerMethodField()

    class Meta:
        model = ListingModel
        fields = [
            # Asosiy ma'lumotlar
            "id",
            "user",
            "name",
            "dealtype",
            "property",
            "property_subtype",

            # Lokatsiya
            "latitude",
            "longitude",
            "address",

            # Xonalar / Qavatlar
            "room_count",
            "floor",
            "total_floors",
            "floors_count",

            # Maydon o'lchamlari
            "apartment_area",
            "house_area",
            "land_area",
            "office_area",
            "building_area",
            "construction_area",
            "room_area",

            # Tamirlash va bino haqida
            "repair_type",
            "building",
            "residential_complex",

            # Narx bilan bog‘liq
            "price_type",
            "price",
            "negotiable",
            "currency",

            # Qo‘shimcha ma’lumot
            "description",
            "phone",
            "images",
            "amenity",

            # Foydalanuvchi holati
            "is_favorited",

            # Top listing
            "is_top",
            "toplisting",
            "top_start_date",
            "top_end_date",

            # Holat
            "is_active",
            "status"
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
    
    def get_toplisting(self, obj):
        return LS.get_toplisting(obj)


class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = BaseListingSerializer.Meta.fields + ["name", "dealtype"]



class RetrieveListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = BaseListingSerializer.Meta.fields




class CreateListingSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
            child=serializers.ImageField(),
            write_only=True,
            required=False
    )    
    amenity = serializers.CharField(write_only=True, required=False)
    toplisting = serializers.IntegerField(required=False, write_only=True)
    

    class Meta:
        model = ListingModel
        fields = [
            # Asosiy ma'lumotlar
            "id",
            "user",
            "name",
            "dealtype",
            "property",
            "property_subtype",

            # Lokatsiya
            "latitude",
            "longitude",
            "address",

            # Xonalar / Qavatlar
            "room_count",
            "floor",
            "total_floors",
            "floors_count",

            # Maydon o'lchamlari
            "apartment_area",
            "house_area",
            "land_area",
            "office_area",
            "building_area",
            "construction_area",
            "room_area",

            # Tamirlash va bino haqida
            "repair_type",
            "building",
            "residential_complex",

            # Narx bilan bog‘liq
            "price_type",
            "price",
            "negotiable",
            "currency",

            # Qo‘shimcha ma’lumot
            "description",
            "phone",
            "amenity",
            "images",

            # Top listing
            "is_top",
            "toplisting",
            "top_start_date",
            "top_end_date",

            # Holat
            "is_active",
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
        top_end_date = validated_data.get("top_end_date")
        toplisting_id = validated_data.pop("toplisting", None)
        
        if toplisting_id:
            try:
                toplisting_obj = ToplistingpriceModel.objects.get(id=toplisting_id)
                validated_data["toplisting"] = toplisting_obj
            except ToplistingpriceModel.DoesNotExist:
                raise serializers.ValidationError("Toplisting ID noto‘g‘ri")


        if top_end_date is None:
                validated_data["is_active"] = True
        else:
            validated_data["is_active"] = False
            
        listing = ListingModel.objects.create(**validated_data)

        if amenity_ids:
            amenities = AmenityModel.objects.filter(id__in=amenity_ids)
            listing.amenity.set(amenities)

        for image in images:
            ListingimageModel.objects.create(listing=listing, image=image)

        send_telegram(listing)

        return listing