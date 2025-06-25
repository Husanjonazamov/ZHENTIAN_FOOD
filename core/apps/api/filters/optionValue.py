from django_filters import rest_framework as filters

from core.apps.api.models import OptionvalueModel


class OptionvalueFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = OptionvalueModel
        fields = [
            "name",
        ]
