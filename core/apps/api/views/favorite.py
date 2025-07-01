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
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError





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
        "toggle": [IsAuthenticated]
    }
    
    action_serializer_class = {
        "list": ListFavoriteSerializer,
        "retrieve": RetrieveFavoriteSerializer,
        "create": CreateFavoriteSerializer,
    }
    
    def get_queryset(self):
        return FavoriteModel.objects.filter(user=self.request.user).order_by('-created_at')
    
    
    
    @action(detail=False, methods=["post"], url_path='toggle', permission_classes=[IsAuthenticated])
    def toggle(self, request):
        listing_id = request.data.get("listing")
        if not listing_id:
            return Response({"detail": "listing_id kiritilmadi"}, status=400)

        user = request.user

        favorite = FavoriteModel.objects.filter(user=user, listing_id=listing_id).first()

        if favorite:
            favorite.delete()
            return Response({
                "status": True,
                "detail": "E'lon favoritedan olib tashlandi",
                "is_favorited": False,
            }, status=200)

        favorite = FavoriteModel.objects.create(user=user, listing_id=listing_id)
        serializer = ListFavoriteSerializer(favorite, context={"request": request})

        return Response(serializer.data)
