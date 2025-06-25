from rest_framework import serializers

from core.apps.api.models import OptionvalueModel


class BaseOptionvalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionvalueModel
        fields = [
            "id",
            "name",
        ]


class ListOptionvalueSerializer(BaseOptionvalueSerializer):
    class Meta(BaseOptionvalueSerializer.Meta): ...


class RetrieveOptionvalueSerializer(BaseOptionvalueSerializer):
    class Meta(BaseOptionvalueSerializer.Meta): ...


class CreateOptionvalueSerializer(BaseOptionvalueSerializer):
    class Meta(BaseOptionvalueSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
