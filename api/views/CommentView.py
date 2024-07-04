from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializer.CommentSerializer import CommentSerializerList, CommentSerializerCreate
from product.models import Comment


class CommentList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.all().filter(product_id=self.request.GET.get('product_id', ''))
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            serializer_class = CommentSerializerList
        else:
            serializer_class = CommentSerializerCreate
        return serializer_class(*args, **kwargs)
