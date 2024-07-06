from django.contrib import admin
from django.utils.html import format_html

from product.models import Category, Product, Comment, Image, Price


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
        '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.poster))

    def _description(self, obj): return format_html('<p>{}</p>'.format(obj.description[:100] + '...'))

    def price(self, obj): return format_html('<p>{}</p>'.format(obj.poster.real_price))

    list_display = ('name', '_description', 'price', 'stock', '_image')

    search_fields = ('pk', 'name', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'content', 'created_at', 'updated_at')
    search_fields = ('product', 'customer', 'content')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    def _image(self, obj): return format_html(
        '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('image', 'title', 'description')
    search_fields = ('title', 'description')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('real_price', 'offer_price', 'discount_percent')
    search_fields = ('real_price', 'offer_price', 'discount_percent')
