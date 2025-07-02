from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from core.apps.api.models.listing import ListingModel
from core.apps.api.serializers.listing import BaseListingSerializer

class ListingSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get("search", "").strip()
        listings = ListingModel.objects.all()

        print("Search query:", search_query)

        if search_query:
            listings = listings.filter(
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

        print("soni:", listings.count())  

        serializer = BaseListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
