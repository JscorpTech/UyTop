from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import BuildingmaterialModel
from core.apps.api.serializers.buildingMaterial import (
    CreateBuildingmaterialSerializer,
    ListBuildingmaterialSerializer,
    RetrieveBuildingmaterialSerializer,
)


@extend_schema(tags=["buildingMaterial"])
class BuildingmaterialView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BuildingmaterialModel.objects.all()
    serializer_class = ListBuildingmaterialSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBuildingmaterialSerializer,
        "retrieve": RetrieveBuildingmaterialSerializer,
        "create": CreateBuildingmaterialSerializer,
    }
