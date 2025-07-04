from django.db.models import Case, When
from django.db.models.query import QuerySet
from core.apps.api.models import ListingModel
from core.apps.api.enums.query import apply_sorting
import random


# is True
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.apps.api.serializers.listing import BaseListingSerializer
from rest_framework.permissions import AllowAny

from itertools import chain
from django.db.models import Case, When
from django.db.models import Case, When, Value, IntegerField




class ListingIsTopView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, pk):
        listing = get_object_or_404(ListingModel, pk=pk)
        
        listing.is_active = True
        listing.is_top = True
        
        
        listing.save()
        
        serializer = BaseListingSerializer(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)



def get_sorted_listings(request):
    top_ids = list(ListingModel.objects.filter(is_top=True).values_list("id", flat=True))
    random.shuffle(top_ids)
    top_ids = top_ids[:3]

    preserved = Case(
        *[When(id=pk, then=Value(pos)) for pos, pk in enumerate(top_ids)],
        default=Value(9999),
        output_field=IntegerField()
    )

    queryset = ListingModel.objects.annotate(
        top_order=preserved
    ).order_by("top_order", "-created_at") 

    return queryset
