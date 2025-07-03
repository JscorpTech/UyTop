from rest_framework import serializers

from core.apps.api.models import CheckModel, ListingModel
from core.apps.api.serializers.listing.enums.send_telegram import send_check


class BaseCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckModel
        fields = [
            "id",
            "listing",
            "image"
        ]


class ListCheckSerializer(BaseCheckSerializer):
    class Meta(BaseCheckSerializer.Meta): ...


class RetrieveCheckSerializer(BaseCheckSerializer):
    class Meta(BaseCheckSerializer.Meta): ...


class CreateCheckSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=ListingModel.objects.all())
    
    class Meta(BaseCheckSerializer.Meta):
        fields = [
            "id",
            "listing",
            "image"
        ]
        
        
    def create(self, validated_data):
        check = super().create(validated_data)
        send_check(check)
        return check
