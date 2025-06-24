from rest_framework import serializers

from core.apps.api.models import ProductModel


class BaseProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "subtitle",
            "category",
            "description",
            "link",
            "image"
        ]
    
    def get_category(self, obj):
        from core.apps.api.serializers import BaseCategorySerializer
        return BaseCategorySerializer(obj.category).data


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    images = serializers.SerializerMethodField()
    class Meta(BaseProductSerializer.Meta):
        fields = BaseProductSerializer.Meta.fields + [
            "content",
            "images",
        ]
        
        
    def get_images(self, obj):
        request = self.context.get("request")
        from core.apps.api.serializers.productImage import BaseProductimageSerializer
        return BaseProductimageSerializer(
            obj.images.all(),
            many=True,
            context={"request": request}
        ).data


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
