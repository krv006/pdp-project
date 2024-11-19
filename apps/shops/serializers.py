from rest_framework.fields import DecimalField
from rest_framework.serializers import ModelSerializer

from shops.models import Category, Product, OrderItem, Order


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'background_image',


class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category, context=self.context).data
        return repr


class OrderItemSerializer(ModelSerializer):
    product = ProductListModelSerializer()

    class Meta:
        model = OrderItem
        fields = "product", "quantity"


class OrderSerializer(ModelSerializer):
    total_price = DecimalField(max_digits=9, decimal_places=2, read_only=True, default=0)

    class Meta:
        model = Order
        fields = 'items', "total_price"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['items'] = OrderItemSerializer(instance.items.all(), many=True).data
        data['total_price'] = sum([i.product.price for i in instance.items.all()])
        return data
