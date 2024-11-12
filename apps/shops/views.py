from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from shops.filters import CategoryFilter, ProductFilter
from shops.models import Category, Product
from shops.serializers import CategoryModelSerializer, ProductListModelSerializer


@extend_schema(tags=['shops'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_class = CategoryFilter


@extend_schema(tags=['shops'])
@extend_schema(description='product')
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    ordering = 'price', '-created_at',
    # TODO mana shu yerda created_at di qoshsa eng yangi eng eski -created_at shunaqa qilish kerak boaldi
    search_fields = 'name', 'description',
    filterset_class = ProductFilter
