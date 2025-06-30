from django_filters import rest_framework as filters

from core.apps.users.models import BotusersModel


class BotusersFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = BotusersModel
        fields = [
            "name",
        ]
