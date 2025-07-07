from rest_framework import serializers

from core.apps.api.models import ToplistingpriceModel


class BaseToplistingpriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToplistingpriceModel
        fields = [
            "id",
            "name",
        ]


class ListToplistingpriceSerializer(BaseToplistingpriceSerializer):
    class Meta(BaseToplistingpriceSerializer.Meta): ...


class RetrieveToplistingpriceSerializer(BaseToplistingpriceSerializer):
    class Meta(BaseToplistingpriceSerializer.Meta): ...


class CreateToplistingpriceSerializer(BaseToplistingpriceSerializer):
    class Meta(BaseToplistingpriceSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
