from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.serializer.OrderSerializer import OrderSerializer
from shoping.models import Order
from product.models import Product, Category

