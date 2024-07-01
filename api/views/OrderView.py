from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from shoping.models import Order
from product.models import Product, Category
from api.serializer.OrderSerializer import OrderSerializer


# get_all_order
class OrderView(APIView):

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        user = request.user
        product_ids = data.get('products', [])
        products = Product.objects.filter(id__in=product_ids)

        if not products:
            return Response({"error": "No valid products provided"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order(user=user)
        order.save()
        order.products.set(products)
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        order_id = request.data.get('order_id')
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
