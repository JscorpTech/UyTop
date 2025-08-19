from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F

from core.apps.api.models import ListingModel
from core.apps.api.serializers.listing import (
    CreateListingSerializer,
    ListListingSerializer,
    RetrieveListingSerializer,
    ListingTopStatusSerializer,
    send_telegram
)
from core.apps.api.enums.query import apply_sorting
from core.apps.api.views.top_listing import get_sorted_listings
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.api.filters.listing import ListingFilter


@extend_schema(tags=["listing"])
class ListingView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListListingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListingFilter

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

    def get_queryset(self):
        queryset = ListingModel.objects.filter(is_active=True)

        if self.action == "list":
            queryset = apply_sorting(queryset, self.request)
            return get_sorted_listings(queryset)

        return apply_sorting(queryset, self.request)

    # ==========================================
    # RETRIEVE /listing/<id>/
    # ==========================================
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views = F('views') + 1  # DB darajasida oshirish
        instance.save(update_fields=['views'])
        instance.refresh_from_db()  # F() ishlatilgandan keyin yangi qiymatni olish
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # ==========================================
    # ME /listing/me/
    # ==========================================
    @action(detail=False, methods=["get"], url_path="me", permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        if not user or not user.is_authenticated:
            return Response({"detail": "Foydalanuvchi aniqlanmadi"}, status=401)

        status_query = request.query_params.get("status")
        queryset = ListingModel.objects.filter(user=user)

        if status_query:
            queryset = queryset.filter(status=status_query)

        queryset = apply_sorting(queryset, request)
        queryset = get_sorted_listings(queryset)

        # Views har safar GET qilinsa oshadi
        queryset.update(views=F('views') + 1)

        serializer = ListListingSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    # ==========================================
    # SEARCH /listing/search/
    # ==========================================
    @action(detail=False, methods=['get'], url_path="search", permission_classes=[IsAuthenticated])
    def search(self, request):
        user = request.user
        if not user or not user.is_authenticated:
            return Response({"detail": "Foydalanuvchi aniqlanmadi"})

        search_query = request.query_params.get("search")
        queryset = ListingModel.objects.filter(is_active=True)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(property__icontains=search_query) |
                Q(property_subtype__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(room_count__icontains=search_query) |
                Q(floor__icontains=search_query) |
                Q(total_floors__icontains=search_query) |
                Q(price__icontains=search_query)
            )

        queryset = apply_sorting(queryset, request)
        queryset = get_sorted_listings(queryset)

        # Views har safar GET qilinsa oshadi
        queryset.update(views=F('views') + 1)

        serializer = ListListingSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    # ==========================================
    # CREATE
    # ==========================================
    @action(detail=False, methods=['post'], url_name="active", permission_classes=[IsAuthenticated])
    def active(self, request):
        serializers = ListingTopStatusSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        listing = serializers.validated_data['listing']
        send_telegram(listing)

        return Response({"success": True})

    # ==========================================
    # DELETE
    # ==========================================
    @action(detail=False, methods=['delete'], url_path="me/delete/(?P<pk>[^/.]+)", permission_classes=[IsAuthenticated])
    def delete_my_listing(self, request, pk=None):
        user = request.user
        try:
            listing = ListingModel.objects.get(pk=pk, user=user)
            listing.delete()
            return Response({"detail": "E'lon o'chirildi"}, status=status.HTTP_200_OK)
        except ListingModel.DoesNotExist:
            return Response({"detail": "E'lon topilmadi yoki sizga tegishli emas"}, status=status.HTTP_404_NOT_FOUND)
