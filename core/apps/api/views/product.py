
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ProductModel
from core.apps.api.serializers.product import CreateProductSerializer, ListProductSerializer, RetrieveProductSerializer
from .pagenation import ProductPagination, BaseViewSetMixin

# filters
from core.apps.api.filters.product import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

# search
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q




@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductSerializer,
        "retrieve": RetrieveProductSerializer,
        "create": CreateProductSerializer,
    }
    
     
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get("search")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )

        return queryset