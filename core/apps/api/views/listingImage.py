from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ListingimageModel
from core.apps.api.serializers.listingImage import (
    CreateListingimageSerializer,
    ListListingimageSerializer,
    RetrieveListingimageSerializer,
)




@extend_schema(tags=["ListingImage"])
class ListingimageView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingimageModel.objects.all()
    serializer_class = ListListingimageSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {
        "create": [IsAuthenticated]
    }
    
    action_serializer_class = {
        "list": ListListingimageSerializer,
        "retrieve": RetrieveListingimageSerializer,
        "create": CreateListingimageSerializer,
    }
