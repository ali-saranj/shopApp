from django.contrib import admin

from shoping.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def _products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    def _customer(self, obj):
        return obj.customer.user.username

    list_display = ('_customer', 'date_ordered', 'complete', 'complete_date', '_products')
