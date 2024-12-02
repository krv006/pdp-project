from rest_framework.fields import BooleanField, ListField, IntegerField
from rest_framework.serializers import ModelSerializer, DecimalField

from users.models import User
from users.serializers import UserModelSerializer, OperatorModelSerializer
from shops.models import Product, Category, Order, OrderItem, Address


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
        fields = 'id', 'product', 'quantity',


class OrderModelSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    # address = AddressModelSerializer(many=True)
    address = ListField(child=IntegerField())
    owner = UserModelSerializer(read_only=True)
    operator = OperatorModelSerializer(read_only=True)

    class Meta:
        model = Order
        fields = 'id', 'payment', 'address', 'owner', 'operator', 'items',

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['items'] = OrderItemSerializer(instance.items.all(), many=True, context=self.context).data
        repr['address'] = AddressModelSerializer(instance.address.all(), many=True, context=self.context).data
        return repr