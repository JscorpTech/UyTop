from django_filters import rest_framework as filters

from core.apps.api.models import ListingModel


class ListingFilter(filters.FilterSet):
    dealtype = filters.CharFilter(field_name='dealtype', lookup_expr='iexact')
    property = filters.CharFilter(field_name="property", lookup_expr="iexact")
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ListingModel
        fields = [
            "dealtype",
            "property"
        ]


# class ListingsubtypeFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = ListingsubtypeModel
#         fields = [
#             "name",
           
        # ]
