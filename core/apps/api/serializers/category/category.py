from rest_framework import serializers

from core.apps.api.models import CategoryModel






class CategoryListWithTotalSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = list(data)
        total_count = self.context.get('total_product_count', 0)

        total = {
            'id': None,
            'total_count': total_count
        }

        result = super().to_representation(data)
        return [total] + result



class BaseCategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "title",
            "image",
            "product_count"
        ]
        list_serializer_class = CategoryListWithTotalSerializer


    def get_product_count(self, obj):
        return obj.product.count()
    

class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class CreateCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta):
        fields = [
            "id",
            "title",
            "image"
        ]
