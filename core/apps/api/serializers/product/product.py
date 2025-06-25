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
    table1 = serializers.SerializerMethodField()
    table2 = serializers.SerializerMethodField()
    
    
    class Meta(BaseProductSerializer.Meta):
        fields = BaseProductSerializer.Meta.fields + [
            "content",
            "images",
            "table1",
            "table2",
        ]
        
        
    def get_images(self, obj):
        request = self.context.get("request")
        from core.apps.api.serializers.productImage import BaseProductimageSerializer
        return BaseProductimageSerializer(
            obj.images.all(),
            many=True,
            context={"request": request}
        ).data



    def get_table1(self, obj):
        options = obj.options.filter(table="table1")
        return [{"key": opt.key, "value": opt.value} for opt in options]
    

    def get_table2(self, obj):
        options = obj.options.filter(table="table2")
        return [{"key": obj.key, "value": obj.value} for obj in options]

class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
