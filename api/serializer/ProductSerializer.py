from rest_framework import serializers

from product.models import Product, Category, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'title', 'description')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'pk', 'name', 'description', 'price', 'stock', 'category', 'created_at', "updated_at", "image", 'poster')
