from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ProductimageModel
from core.apps.api.serializers.productImage import (
    CreateProductimageSerializer,
    ListProductimageSerializer,
    RetrieveProductimageSerializer,
)


@extend_schema(tags=["productImage"])
class ProductimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductimageModel.objects.all()
    serializer_class = ListProductimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductimageSerializer,
        "retrieve": RetrieveProductimageSerializer,
        "create": CreateProductimageSerializer,
    }
