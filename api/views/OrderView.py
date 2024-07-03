from rest_framework.permissions import IsAuthenticated
from shoping.models import Order
from api.serializer.OrderSerializer import OrderSerializer, OrderSerializerList, OrderSerializerCreate
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# get_all_order
class OrderView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.all().filter(customer__user=self.request.user)
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            serializer_class = OrderSerializerList
        else:
            serializer_class = OrderSerializerCreate
        return serializer_class(*args, **kwargs)


class OrderDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Order.objects.all().filter(customer__user=self.request.user)
        return queryset

    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
