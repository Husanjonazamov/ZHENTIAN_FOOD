from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import OptionvalueModel
from core.apps.api.serializers.optionValue import (
    CreateOptionvalueSerializer,
    ListOptionvalueSerializer,
    RetrieveOptionvalueSerializer,
)


@extend_schema(tags=["optionValue"])
class OptionvalueView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OptionvalueModel.objects.all()
    serializer_class = ListOptionvalueSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOptionvalueSerializer,
        "retrieve": RetrieveOptionvalueSerializer,
        "create": CreateOptionvalueSerializer,
    }
