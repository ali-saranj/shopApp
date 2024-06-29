from django.contrib import admin
from django.utils.html import format_html

from product.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def _image(self, obj): return format_html(
        '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    def _description(self, obj): return format_html('<p>{}</p>'.format(obj.description[:100] + '...'))

    list_display = ('name', '_description', '_image')

    search_fields = ('pk', 'name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def _image(self, obj): return format_html(
        '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    def _description(self, obj): return format_html('<p>{}</p>'.format(obj.description[:100] + '...'))

    list_display = ('name', '_description', 'price', 'stock', 'category', '_image')

    search_fields = ('pk', 'name', 'description')
