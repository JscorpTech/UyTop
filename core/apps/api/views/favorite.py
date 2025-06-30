from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import FavoriteModel
from core.apps.api.serializers.favorite import (
    CreateFavoriteSerializer,
    ListFavoriteSerializer,
    RetrieveFavoriteSerializer,
)
from core.apps.users.permissions.botusers import BotusersPermission


@extend_schema(tags=["favorite"])
class FavoriteView(BaseViewSetMixin, ModelViewSet):
    queryset = FavoriteModel.objects.all()
    serializer_class = ListFavoriteSerializer
    permission_classes = [AllowAny, BotusersPermission]
    
    

    action_permission_classes = {
        "create": [BotusersPermission],
        "list": [BotusersPermission],
        "retrieve": [BotusersPermission],
        "destroy": [BotusersPermission],
    }
    
    action_serializer_class = {
        "list": ListFavoriteSerializer,
        "retrieve": RetrieveFavoriteSerializer,
        "create": CreateFavoriteSerializer,
    }
    
    def get_queryset(self):
        return FavoriteModel.objects.filter(user=self.request.bot_user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.bot_user)
