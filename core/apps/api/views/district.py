from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import DistrictModel
from core.apps.api.serializers.district import (
    CreateDistrictSerializer,
    ListDistrictSerializer,
    RetrieveDistrictSerializer,
)


@extend_schema(tags=["District"])
class DistrictView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = DistrictModel.objects.all()
    serializer_class = ListDistrictSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDistrictSerializer,
        "retrieve": RetrieveDistrictSerializer,
        "create": CreateDistrictSerializer,
    }
