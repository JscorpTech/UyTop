from django.db.models import Q, FloatField
from django.db.models.functions import Cast
from django_filters import rest_framework as filters
from core.apps.api.models import ListingModel
from core.apps.api.enums.listing import ListingStatus

class ListingFilter(filters.FilterSet):
    dealtype = filters.CharFilter(field_name="dealtype", lookup_expr="iexact")
    room_count = filters.CharFilter(field_name="room_count", lookup_expr="iexact")
    repairType = filters.CharFilter(field_name="repair_type", lookup_expr="iexact")
    floor = filters.CharFilter(field_name="floor", lookup_expr="iexact")
    total_floors = filters.CharFilter(field_name="total_floors", lookup_expr="iexact")
    price_type = filters.CharFilter(field_name="price_type", lookup_expr="iexact")
    building = filters.NumberFilter(field_name="building__id")
    amenity = filters.BaseInFilter(field_name="amenity__id", lookup_expr="in")
    region = filters.CharFilter(method="filter_region")
    property = filters.CharFilter(field_name="property", lookup_expr="iexact")
    property_subtype = filters.CharFilter(field_name="property_subtype", lookup_expr="iexact")

    price_start = filters.NumberFilter(method="filter_price")
    price_end = filters.NumberFilter(method="filter_price")

    area_start = filters.NumberFilter(method="filter_area")
    area_end = filters.NumberFilter(method="filter_area")
    is_top = filters.BooleanFilter(field_name="is_top")
    status = filters.ChoiceFilter(choices=ListingStatus.choices)

    class Meta:
        model = ListingModel
        fields = [
            "dealtype",
            "room_count",
            "repairType",
            "region",
            "floor",
            "total_floors",
            "price_type",
            "building",
            "property",
            "property_subtype",
            "amenity",
            "is_top",
            "status",
        ]

    def filter_price(self, queryset, name, value):
        if value is None:
            return queryset
        
        # Annotate with numeric price for correct comparison
        # Using a subquery cast or simple annotation
        queryset = queryset.annotate(
            price_numeric=Cast("price", output_field=FloatField())
        )
        
        if name == "price_start":
            return queryset.filter(price_numeric__gte=value)
        if name == "price_end":
            return queryset.filter(price_numeric__lte=value)
        return queryset

    def filter_area(self, queryset, name, value):
        if value is None:
            return queryset
        
        # We check multiple area fields since different types of listings use different fields
        # But prioritize apartment_area as requested
        q_fields = [
            "apartment_area", "house_area", "land_area", 
            "office_area", "building_area", "construction_area", "room_area"
        ]
        
        if name == "area_start":
            q_obj = Q()
            for field in q_fields:
                q_obj |= Q(**{f"{field}__gte": value})
            return queryset.filter(q_obj)
        
        if name == "area_end":
            q_obj = Q()
            for field in q_fields:
                q_obj |= Q(**{f"{field}__lte": value})
            return queryset.filter(q_obj)
        
        return queryset

    def filter_region(self, queryset, name, value):
        if not value:
            return queryset
        
        val_lower = value.lower()
        if val_lower == "toshkent" or val_lower == "ташкент":
            # Return all listings that contain "Toshkent" in either Latin or Cyrillic
            return queryset.filter(Q(region__icontains="Toshkent") | Q(region__icontains="Ташкент"))
        
        return queryset.filter(region__iexact=value)


# class ListingsubtypeFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = ListingsubtypeModel
#         fields = [
#             "name",
           
        # ]
