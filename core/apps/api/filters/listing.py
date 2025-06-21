from django_filters import rest_framework as filters

from core.apps.api.models import ListingModel, ListingsubtypeModel


class ListingFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ListingModel
        fields = [
            "name",
        ]


class ListingsubtypeFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ListingsubtypeModel
        fields = [
            "name",
        ]
