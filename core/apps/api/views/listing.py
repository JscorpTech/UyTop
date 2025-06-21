from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ListingModel
from core.apps.api.serializers.listing import (
    CreateListingSerializer,
    ListListingSerializer,
    RetrieveListingSerializer,
)


@extend_schema(tags=["listing"])
class ListingView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListListingSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListListingSerializer,
        "retrieve": RetrieveListingSerializer,
        "create": CreateListingSerializer,
    }

