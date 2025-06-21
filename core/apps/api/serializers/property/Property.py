from rest_framework import serializers

from core.apps.api.models import PropertyModel


class BasePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = [
            "id",
            "name",
        ]


class ListPropertySerializer(BasePropertySerializer):
    class Meta(BasePropertySerializer.Meta): ...


class RetrievePropertySerializer(BasePropertySerializer):
    class Meta(BasePropertySerializer.Meta): ...


class CreatePropertySerializer(BasePropertySerializer):
    class Meta(BasePropertySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
