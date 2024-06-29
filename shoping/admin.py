from django.contrib import admin

from shoping.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    def customer(self, obj):
        return obj.customer.username

    list_display = ('customer', 'date_ordered', 'complete', 'complete_date', 'products')
