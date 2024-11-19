from django.urls import path

from shops.views import CategoryListCreateAPIView, ProductListCreateAPIView, ProductsByCategoryView, OrderListAPIView, \
    OrderItemListCreateAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('categories/<int:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('order-list', OrderListAPIView.as_view(), name='order-list'),
    path('order-item', OrderItemListCreateAPIView.as_view(), name='order-item'),

]
