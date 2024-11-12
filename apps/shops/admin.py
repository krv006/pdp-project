from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shops.models import Product, Category, Address, Brand, Payment, Image, SiteSettings, QuickOrder


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    pass


@admin.register(QuickOrder)
class QuickOrderAdmin(ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    pass
