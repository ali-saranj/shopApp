from django.db import models
from product.models import Product
from user.models import Customer


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, editable=False)
    complete_date = models.DateTimeField(null=True, blank=True, editable=False)
    pay_method = models.IntegerField(choices=[(1, 'Cash'), (2, 'Online')], default=1)
    products = models.ManyToManyField(Product, related_name='orders')

    def __str__(self):
        return f" customer: {self.customer} - products: {self.products} - date: {self.date_ordered}"
