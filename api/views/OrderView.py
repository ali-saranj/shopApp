from rest_framework.decorators import api_view
from rest_framework.views import APIView
from shoping.models import Order
from product.models import Product, Category


@api_view(["GET"])
def Order_view(request):
    order = Order.products.objects.all()
