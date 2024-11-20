from rest_framework.serializers import ModelSerializer, DecimalField

from users.serializers import UserModelSerializer
from .models import Product, Category, Order, OrderItem, Address


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'background_image',


class ProductListModelSerializer(ModelSerializer):
    category = CategoryModelSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'discount_price', 'size', 'poll', 'color',
                  'material', 'lining', 'made_from', 'category',)


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    product = ProductListModelSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    address = AddressModelSerializer(read_only=True)
    owner = UserModelSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'payment', 'address', 'owner', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = OrderItemSerializer(instance.items.all(), many=True).data
        return representation
