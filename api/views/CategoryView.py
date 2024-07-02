from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from api.serializer.CategorySerializer import CategorySerializerList, CategorySerializerDefile
from product.models import Category


class CategoryList(ListAPIView):
    serializer_class = CategorySerializerList
    queryset = Category.objects.all()


class CategoryDetail(RetrieveAPIView):
    serializer_class = CategorySerializerDefile
    queryset = Category.objects.all()

