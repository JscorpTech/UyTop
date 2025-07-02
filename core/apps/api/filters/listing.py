from django_filters import rest_framework as filters
from core.apps.api.models import ListingModel


class ListingFilter(filters.FilterSet):
    dealtype = filters.CharFilter(field_name="dealtype", lookup_expr="iexact")
    room_count = filters.CharFilter(field_name="room_count", lookup_expr="iexact")
    repairType = filters.CharFilter(field_name="repair_type", lookup_expr="iexact")
    floor = filters.CharFilter(field_name="floor", lookup_expr="iexact")
    total_floors = filters.CharFilter(field_name="total_floors", lookup_expr="iexact")
    price_type = filters.CharFilter(field_name="price_type", lookup_expr="iexact")
    building = filters.NumberFilter(field_name="building__id")
    amenity = filters.BaseInFilter(field_name="amenity__id", lookup_expr="in")

    price_start = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_end = filters.NumberFilter(field_name="price", lookup_expr="lte")

    area_start = filters.NumberFilter(field_name="land_area", lookup_expr="gte")
    area_end = filters.NumberFilter(field_name="land_area", lookup_expr="lte")

    class Meta:
        model = ListingModel
        fields = [
            "dealtype",
            "room_count",
            "repairType",
            "floor",
            "total_floors",
            "price_type",
            "building",
            "amenity",
        ]


# class ListingsubtypeFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = ListingsubtypeModel
#         fields = [
#             "name",
           
        # ]
