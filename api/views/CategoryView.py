from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializer.CategorySerializer import CategorySerializerList, CategorySerializerDefile
from product.models import Category


class CategoryList(ListAPIView):
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        queryset = Category.objects.all().filter(
            Q(name__contains=query) |
            Q(description__contains=query)
        )
        return queryset

    serializer_class = CategorySerializerList


class CategoryDetail(RetrieveAPIView):
    serializer_class = CategorySerializerDefile
    queryset = Category.objects.all()
