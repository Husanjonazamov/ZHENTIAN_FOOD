from django_filters import rest_framework as filters

from core.apps.api.models import ProductimageModel


class ProductimageFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProductimageModel
        fields = [
            "name",
        ]
