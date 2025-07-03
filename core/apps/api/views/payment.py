from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from core.apps.api.models import CheckModel, PaymentModel
from core.apps.api.serializers.payment import (
    CreateCheckSerializer,
    CreatePaymentSerializer,
    ListCheckSerializer,
    ListPaymentSerializer,
    RetrieveCheckSerializer,
    RetrievePaymentSerializer,
)


@extend_schema(tags=["payment"])
class PaymentView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PaymentModel.objects.all()
    serializer_class = ListPaymentSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPaymentSerializer,
        "retrieve": RetrievePaymentSerializer,
        "create": CreatePaymentSerializer,
    }


@extend_schema(tags=["check"])
class CheckView(BaseViewSetMixin, ModelViewSet):
    queryset = CheckModel.objects.all()
    serializer_class = ListCheckSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCheckSerializer,
        "retrieve": RetrieveCheckSerializer,
        "create": CreateCheckSerializer,
    }
