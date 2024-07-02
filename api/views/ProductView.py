from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from api.serializer.ProductSerializer import ProductSerializer
from product.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSearch(APIView):
    def get(self, request, format=None):
        try:
            query = request.GET.get('query', '')
            products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404

