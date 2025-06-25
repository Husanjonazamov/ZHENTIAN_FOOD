from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import OptionsModel
from core.apps.api.serializers.options import CreateOptionsSerializer, ListOptionsSerializer, RetrieveOptionsSerializer


@extend_schema(tags=["OPtions"])
class OptionsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OptionsModel.objects.all()
    serializer_class = ListOptionsSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOptionsSerializer,
        "retrieve": RetrieveOptionsSerializer,
        "create": CreateOptionsSerializer,
    }
