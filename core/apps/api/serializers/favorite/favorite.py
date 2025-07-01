from rest_framework import serializers
from core.apps.users.serializers.botusers import BaseBotusersSerializer
from core.apps.api.serializers.listing import BaseListingSerializer
from core.apps.api.models import FavoriteModel, ListingModel


class BaseFavoriteSerializer(serializers.ModelSerializer):
    listing = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = FavoriteModel
        fields = [
            "id",
            "user",
            "listing"
        ]

    def get_listing(self, obj):
        request = self.context.get("request")
        return BaseListingSerializer(obj.listing, context={"request": request}).data 
    
    def get_user(self, obj):
        return BaseBotusersSerializer(obj.user).data
        


class ListFavoriteSerializer(BaseFavoriteSerializer):
    class Meta(BaseFavoriteSerializer.Meta): ...


class RetrieveFavoriteSerializer(BaseFavoriteSerializer):
    class Meta(BaseFavoriteSerializer.Meta): ...


class CreateFavoriteSerializer(BaseFavoriteSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=ListingModel.objects.all())
    
    class Meta(BaseFavoriteSerializer.Meta):
        extra_kwargs = {
            "user": {"read_only": True},
            "listing": {"required": True},
        }