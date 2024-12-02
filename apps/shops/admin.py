import os

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from shops.models import Product, Category, Address, Brand, Payment, Image, SiteSettings, QuickOrder, Order, OrderItem


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = 'name', 'price', 'size', 'poll', 'color',
    list_editable = 'size', 'poll', 'color',
    list_filter = 'created_at',
    ordering = '-created_at',
    readonly_fields = 'created_at',


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = 'name',
    ordering = '-created_at',


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone_number', 'email',
    list_editable = 'email', 'phone_number',


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    pass


@admin.register(QuickOrder)
class QuickOrderAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = 'name', 'image',
    list_editable = 'image',
    # @admin.action(description='rasm')
    # def img(self, obj:Brand):
    #     a = obj.image
    #     if a:
    #         return mark_safe(f'<img src="{a.url}" alt="Description of the image" width="500" height="300">')
    #     else:
    #         return None
