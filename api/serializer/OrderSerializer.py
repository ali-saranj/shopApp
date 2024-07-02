from rest_framework import serializers
from shoping.models import Order
from product.models import Product


class OrderSerializerList(serializers.ModelSerializer):
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'price', 'image')

    products = ProductSerializer(required=True, many=True)

    class Meta:
        model = Order
        fields = ('customer', 'pay_method', 'products')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'pay_method', 'products')
