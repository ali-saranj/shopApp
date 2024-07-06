from django.db import models

from manage import main
from user.models import Customer


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Category/%m/')
    description = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/Product/%m/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2083)

    def __str__(self):
        return f"{self.title}"


class Price(models.Model):
    real_price = models.FloatField()
    offer_price = models.FloatField(null=True, blank=True)
    discount_percent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f" real_price: {self.real_price} - offer_price: {self.offer_price}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2083)
    price = models.OneToOneField(Price, on_delete=models.PROTECT, related_name='products')
    stock = models.IntegerField()
    category = models.ManyToManyField(Category, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ManyToManyField(Image, related_name='products')

    @property
    def poster(self):
        return self.image.first().image.url

    def __str__(self):
        return f" name:{self.name} - category: {self.category} - price: {self.price}"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='comments')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='comments')
    content = models.CharField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" product: {self.product} - customer: {self.customer} - content: {self.content}"
