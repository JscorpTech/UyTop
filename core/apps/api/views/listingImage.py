from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ListingimageModel
from core.apps.api.serializers.listingImage import (
    CreateListingimageSerializer,
    ListListingimageSerializer,
    RetrieveListingimageSerializer,
)


@extend_schema(tags=["ListingImage"])
class ListingimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ListingimageModel.objects.all()
    serializer_class = ListListingimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListListingimageSerializer,
        "retrieve": RetrieveListingimageSerializer,
        "create": CreateListingimageSerializer,
    }
