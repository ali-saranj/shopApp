from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer.CategorySerializer import CategorySerializerList, CategorySerializerDefile
from product.models import Category


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializerList(categories, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializerDefile(category)
        return Response(serializer.data)

