from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import PropertyModel, PropertysubtypeModel
from core.apps.api.serializers.property import (
    CreatePropertySerializer,
    ListPropertySerializer,
    RetrievePropertySerializer,
    ListPropertysubtypeSerializer,
    RetrievePropertysubtypeSerializer,
    CreatePropertysubtypeSerializer

)


@extend_schema(tags=["Property"])
class PropertyView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = ListPropertySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPropertySerializer,
        "retrieve": RetrievePropertySerializer,
        "create": CreatePropertySerializer,
    }



@extend_schema(tags=["PropertySubType"])
class PropertysubtypeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PropertysubtypeModel.objects.all()
    serializer_class = ListPropertysubtypeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPropertysubtypeSerializer,
        "retrieve": RetrievePropertysubtypeSerializer,
        "create": CreatePropertysubtypeSerializer,
    }
