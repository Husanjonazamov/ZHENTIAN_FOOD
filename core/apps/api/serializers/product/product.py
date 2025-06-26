from rest_framework import serializers

from core.apps.api.models import ProductModel
from django.utils.text import slugify


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
            "image",
            "popular"
            
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
            "table"
        ]
        
        
    def get_images(self, obj):
        request = self.context.get("request")
        from core.apps.api.serializers.productImage import BaseProductimageSerializer
        return BaseProductimageSerializer(
            obj.images.all(),
            many=True,
            context={"request": request}
        ).data



   

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "title",
            "slug",
            "subtitle",
            "category",
            "description",
            "content",
            "video_url",
            "image",
            "link",
            "popular",
            "is_new",
            "rate",
        ]



    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["title"])
        return super().create(validated_data)