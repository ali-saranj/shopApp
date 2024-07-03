"""
URL configuration for shopApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework.authtoken import views

from api.views.UserView import *
from api.views.ProductView import *
from api.views.CategoryView import *
from api.views.OrderView import *

urlpatterns = (
    [
        # productLink
        path('products/', ProductList.as_view(), name='productList'),
        path('product/<int:pk>', ProductDetail.as_view(), name='productDetail'),

        # categoryLink
        path('categories/', CategoryList.as_view(), name='categoryList'),
        path('category/<int:pk>', CategoryDetail.as_view(), name='categoryDetail'),
        # path('categorySearch/<str:name>/<str:description>', CategorySearch.as_view(), name='categorySearch'),

        # orderLink
        path('orders/', OrderView.as_view(), name='order-view'),
        path('order/<int:pk>', OrderDetail.as_view(), name='orderDetail'),
        # path('orderSearch/<str:name>/<str:description>', OrderSearch.as_view(), name='orderSearch'),
        # path('orderCreate/', OrderCreate.as_view(), name='orderCreate'),
        # path('orderUpdate/<int:pk>', OrderUpdate.as_view(), name='orderUpdate'),
        # path('orderDelete/<int:pk>', OrderDelete.as_view(), name='orderDelete'),

        # userLink
        path('register_user/', UserRegister.as_view(), name="user_register"),
        path('login_user/', UserLogin.as_view(), name="user_login"),

        # attention
        path('api-token-auth/', views.obtain_auth_token)
    ]
)
