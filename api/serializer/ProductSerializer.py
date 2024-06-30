from rest_framework import serializers

from product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('pk', 'name', 'description', 'price', 'stock', 'category', 'created_at', "updated_at", "image",)
