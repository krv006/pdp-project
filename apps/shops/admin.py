import os

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from shops.models import Product, Category, Address, Brand, Payment, Image, SiteSettings, QuickOrder, Order


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


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
