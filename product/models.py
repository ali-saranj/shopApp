from django.db import models

from manage import main
from user.models import Customer


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Category/%m/')
    description = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2083)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/Product/%m/')

    def __str__(self):
        return f" name:{self.name} - category: {self.category} - price: {self.price}"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='comments')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='comments')
    content = models.CharField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
