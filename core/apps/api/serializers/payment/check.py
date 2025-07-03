from rest_framework import serializers

from core.apps.api.models import CheckModel, ListingModel


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
