from rest_framework import serializers

from core.apps.api.models import BuildingmaterialModel


class BaseBuildingmaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingmaterialModel
        fields = [
            "id",
            "name",
        ]


class ListBuildingmaterialSerializer(BaseBuildingmaterialSerializer):
    class Meta(BaseBuildingmaterialSerializer.Meta): ...


class RetrieveBuildingmaterialSerializer(BaseBuildingmaterialSerializer):
    class Meta(BaseBuildingmaterialSerializer.Meta): ...


class CreateBuildingmaterialSerializer(BaseBuildingmaterialSerializer):
    class Meta(BaseBuildingmaterialSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
