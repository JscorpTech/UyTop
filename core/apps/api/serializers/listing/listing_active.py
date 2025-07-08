from rest_framework import serializers
from core.apps.api.models import ListingModel, ToplistingpriceModel


class ListingTopStatusSerializer(serializers.Serializer):
    listing = serializers.IntegerField()
    toplisting = serializers.IntegerField()

    def validate(self, attrs):
        listing = attrs.get('listing')
        toplisting = attrs.get('toplisting')

        try:
            listing = ListingModel.objects.get(id=listing)
        except ListingModel.DoesNotExist:
            raise serializers.ValidationError("Bunday listing mavjud emas")

        try:
            toplisting = ToplistingpriceModel.objects.get(id=toplisting)
        except ToplistingpriceModel.DoesNotExist:
            raise serializers.ValidationError("Bunday toplisting mavjud emas")

        attrs['listing'] = listing
        attrs['toplisting'] = toplisting
        return attrs
