from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer.ProductSerializer import ProductSerializer
from product.models import Product


class ProductList(APIView):
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)


class ProductSearch(APIView):
    def get(self, request, format=None):
        try:
            query = request.GET.get('query', '')
            snippets = Product.objects.filter(name__contains=query, description__contains=query,category__name__contains=query)
            serializer = ProductSerializer(snippets, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404
