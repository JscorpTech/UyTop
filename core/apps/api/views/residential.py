from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ResidentialcomplexModel
from core.apps.api.serializers.residential import (
    CreateResidentialcomplexSerializer,
    ListResidentialcomplexSerializer,
    RetrieveResidentialcomplexSerializer,
)


@extend_schema(tags=["ResidentialComplex"])
class ResidentialcomplexView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ResidentialcomplexModel.objects.all()
    serializer_class = ListResidentialcomplexSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListResidentialcomplexSerializer,
        "retrieve": RetrieveResidentialcomplexSerializer,
        "create": CreateResidentialcomplexSerializer,
    }
