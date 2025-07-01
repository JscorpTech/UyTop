from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ListingModel
from core.apps.api.serializers.listing import (
    CreateListingSerializer,
    ListListingSerializer,
    RetrieveListingSerializer,
)


# me
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




@extend_schema(tags=["listing"])
class ListingView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListListingSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {
        "create": [IsAuthenticated]
    }
    
    action_serializer_class = {
        "list": ListListingSerializer,
        "retrieve": RetrieveListingSerializer,
        "create": CreateListingSerializer,
    }
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(detail=False, methods=["get"], url_path="me", permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user  
        if not user or not user.is_authenticated:
            return Response({"detail": "Foydalanuvchi aniqlanmadi"}, status=401)

        listings = ListingModel.objects.filter(user=user)
        serializer = ListListingSerializer(listings, many=True)
        return Response(serializer.data)
    