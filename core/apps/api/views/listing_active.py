from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.apps.api.models import ListingModel, ToplistingpriceModel
from core.apps.api.serializers.listing import ListingTopStatusSerializer
from core.apps.api.serializers.listing.enums.send_telegram import send_telegram



class ListingTopStatusView(APIView):
    def post(self, request):
        serializer = ListingTopStatusSerializer(data=request.data)
        if serializer.is_valid():
            listing = serializer.validated_data['listing']

           
            send_telegram(listing)

            return Response({"status": "success"}, status=200)
        return Response(serializer.errors, status=400)


