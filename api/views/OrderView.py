from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from shoping.models import Order
from product.models import Product, Category
from api.serializer.OrderSerializer import OrderSerializer


# get_all_order
class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        orders = Order.objects.filter(customer=request.user.customer)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user = request.user.customer
        product_ids = data.get('products', [])
        products = Product.objects.filter(id__in=product_ids)

        if not products:
            return Response({"error": "No valid products provided"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order(customer=user)
        order.save()
        order.products.set(products)
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        order_id = request.data.get('order_id')
        try:
            order = Order.objects.get(id=order_id, customer=request.user.customer)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
