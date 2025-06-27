from django_filters import rest_framework as filters

from core.apps.api.models import ProductModel


class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name="category_id")
    popular = filters.BooleanFilter(field_name="popular")
    
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProductModel
        fields = [
            "name",
            "category",
            "popular"
        ]
