from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import AmenityModel
from core.apps.api.serializers.amenity import CreateAmenitySerializer, ListAmenitySerializer, RetrieveAmenitySerializer


@extend_schema(tags=["Amenity"])
class AmenityView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AmenityModel.objects.all()
    serializer_class = ListAmenitySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListAmenitySerializer,
        "retrieve": RetrieveAmenitySerializer,
        "create": CreateAmenitySerializer,
    }
