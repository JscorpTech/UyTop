from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import FavoriteModel
from core.apps.api.serializers.favorite import (
    CreateFavoriteSerializer,
    ListFavoriteSerializer,
    RetrieveFavoriteSerializer,
)



@extend_schema(tags=["favorite"])
class FavoriteView(BaseViewSetMixin, ModelViewSet):
    queryset = FavoriteModel.objects.all()
    serializer_class = ListFavoriteSerializer
    permission_classes = [IsAuthenticated]
    
    

    action_permission_classes = {
        "create": [IsAuthenticated],
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }
    
    action_serializer_class = {
        "list": ListFavoriteSerializer,
        "retrieve": RetrieveFavoriteSerializer,
        "create": CreateFavoriteSerializer,
    }
    
    def get_queryset(self):
        return FavoriteModel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
