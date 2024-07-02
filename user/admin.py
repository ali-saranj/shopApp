from django.contrib import admin

from user.models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'postal_code', 'country', 'phone')
