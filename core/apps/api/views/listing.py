from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ListingModel
from core.apps.api.serializers.listing import (
    CreateListingSerializer,
    ListListingSerializer,
    RetrieveListingSerializer,
)
from core.apps.users.permissions.botusers import BotusersPermission

# me
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




@extend_schema(tags=["listing"])
class ListingView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListListingSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {
        "create": [AllowAny, BotusersPermission]
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

    @action(detail=False, methods=["get"], url_path="me", permission_classes=[BotusersPermission])
    def me(self, request):
        user = getattr(request, "bot_user", None)
        if not user:
            return Response({"detail": "Foydalanuvchi aniqlanmadi"}, status=401)
        
        listings = ListingModel.objects.filter(bot_user=user)
        serializer = ListListingSerializer(listings, many=True)
        return Response(serializer.data)
    