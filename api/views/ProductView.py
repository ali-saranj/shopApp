from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from api.serializer.ProductSerializer import ProductSerializer
from product.models import Product


class ProductList(ListAPIView):
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        queryset = Product.objects.all().filter(
            Q(name__contains=query) |
            Q(description__contains=query) |
            Q(category__name__contains=query) |
            Q(category__description__contains=query)
        )
        return queryset
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
