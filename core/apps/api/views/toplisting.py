from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ToplistingpriceModel
from core.apps.api.serializers.toplisting import (
    CreateToplistingpriceSerializer,
    ListToplistingpriceSerializer,
    RetrieveToplistingpriceSerializer,
)


@extend_schema(tags=["TopListingPrice"])
class ToplistingpriceView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ToplistingpriceModel.objects.all()
    serializer_class = ListToplistingpriceSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListToplistingpriceSerializer,
        "retrieve": RetrieveToplistingpriceSerializer,
        "create": CreateToplistingpriceSerializer,
    }
