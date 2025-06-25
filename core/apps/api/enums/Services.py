from ..serializers.property import BasePropertySerializer
from ..serializers.listingImage import BaseListingimageSerializer
from ..serializers.amenity import BaseAmenitySerializer



class ListingServices:
    
    @staticmethod
    def get_property(property_obj):
        return BasePropertySerializer(property_obj.property).data if property_obj else None
    
    
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