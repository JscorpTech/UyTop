from django_filters import rest_framework as filters

from core.apps.api.models import PropertyModel


class PropertyFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PropertyModel
        fields = [
            "name",
        ]
