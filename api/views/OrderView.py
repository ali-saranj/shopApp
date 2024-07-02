from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from shoping.models import Order
from product.models import Product, Category
from api.serializer.OrderSerializer import OrderSerializer, OrderSerializerList
from rest_framework.generics import ListCreateAPIView


# get_all_order
class OrderView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            serializer_class = OrderSerializerList
        else:
            serializer_class = OrderSerializer
        return serializer_class(*args, **kwargs)
