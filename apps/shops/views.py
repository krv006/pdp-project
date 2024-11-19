from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shops.filters import CategoryFilter, ProductFilter
from shops.models import Category, Product, Order, OrderItem
from shops.serializers import CategoryModelSerializer, ProductListModelSerializer, OrderSerializer


@extend_schema(tags=['shops'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = IsAuthenticated,
    filterset_class = CategoryFilter


@extend_schema(tags=['shops'])
@extend_schema(description='product')
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    permission_classes = IsAuthenticated,
    filterset_class = ProductFilter
    search_fields = 'name', 'description',
    ordering_fields = 'price', 'created_at',
    ordering = '-created_at',
    # TODO mana shu yerda created_at di qoshsa eng yangi eng eski -created_at shunaqa qilish kerak boaldi


@extend_schema(tags=['shops'])
class ProductsByCategoryView(ListAPIView):
    serializer_class = ProductListModelSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)


# @extend_schema(tags=['order'])
# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.prefetch_related('items__product').all()
#     serializer_class = OrderSerializer
#
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         order_items = data.pop('items', [])
#         order = Order.objects.create(**data)
#
#         for item in order_items:
#             product = Product.objects.get(id=item['product'])
#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 quantity=item['quantity']
#             )
#
#         serializer = self.get_serializer(order)
#         return Response(serializer.data)

@extend_schema(tags=['order'])
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=201)
