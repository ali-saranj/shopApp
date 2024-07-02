from rest_framework.views import APIView
from user.models import Customer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from api.serializer.UserSerializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Register User
class UserRegister(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


# Login User
class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        customer = user.customer
        customer_serializer = CustomerSerializer(customer)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'customer': customer_serializer.data},
                        status=HTTP_200_OK)
