from ..serializers.buildingMaterial import BaseBuildingmaterialSerializer
from ..serializers.listingImage import BaseListingimageSerializer
from ..serializers.amenity import BaseAmenitySerializer



class ListingServices:
    @staticmethod
    def get_building(building_obj):
        return BaseBuildingmaterialSerializer(building_obj.building).data if building_obj else None
    
    
    @staticmethod
    def get_images(images_obj, request):
        return BaseListingimageSerializer(
            images_obj.images.all(),
            many=True,
            context={"request": request}
            ).data
    

    @staticmethod
    def get_amenity(amenity_obj):
        return BaseAmenitySerializer(
            amenity_obj.amenity,
            many=True
        ).data