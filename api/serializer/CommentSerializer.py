from rest_framework import serializers
from product.models import Comment


class CommentSerializerList(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'customer', 'content', 'created_at', 'updated_at')


class CommentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'product', 'customer', 'content', 'created_at', 'updated_at')
