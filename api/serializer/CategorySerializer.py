from rest_framework import serializers
from product.models import Category, Product


class CategorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')


class CategorySerializerDefile(serializers.ModelSerializer):
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('pk', 'name', 'description', 'price', 'stock', 'category', 'created_at', "updated_at", "image",)

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'products')
