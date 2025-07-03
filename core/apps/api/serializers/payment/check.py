from rest_framework import serializers

from core.apps.api.models import CheckModel


class BaseCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckModel
        fields = [
            "id",
            "name",
        ]


class ListCheckSerializer(BaseCheckSerializer):
    class Meta(BaseCheckSerializer.Meta): ...


class RetrieveCheckSerializer(BaseCheckSerializer):
    class Meta(BaseCheckSerializer.Meta): ...


class CreateCheckSerializer(BaseCheckSerializer):
    class Meta(BaseCheckSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
