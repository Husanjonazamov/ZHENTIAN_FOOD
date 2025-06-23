from rest_framework import serializers

from core.apps.api.models import ProductimageModel


class BaseProductimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductimageModel
        fields = [
            "id",
            "product",
            "image",
        ]
        
    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if request else obj.iamge.url


class ListProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta): ...


class RetrieveProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta): ...


class CreateProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta):
        fields = [
            "id",
            "product",
            "image"
        ]
