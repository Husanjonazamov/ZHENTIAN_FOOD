from rest_framework import serializers

from core.apps.api.models import OptionsModel


class BaseOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionsModel
        fields = [
            "id",
            "key",
            "value",
            
        ]
        
   

class ListOptionsSerializer(BaseOptionsSerializer):
    class Meta(BaseOptionsSerializer.Meta): ...


class RetrieveOptionsSerializer(BaseOptionsSerializer):
    class Meta(BaseOptionsSerializer.Meta): ...


class CreateOptionsSerializer(BaseOptionsSerializer):
    class Meta(BaseOptionsSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
