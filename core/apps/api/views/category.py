from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import CategoryModel, ProductModel
from core.apps.api.serializers.category import (
    CreateCategorySerializer,
    ListCategorySerializer,
    RetrieveCategorySerializer,
)



@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCategorySerializer,
        "retrieve": RetrieveCategorySerializer,
        "create": CreateCategorySerializer,
    }
    

