from django.urls import path
from rest_framework.routers import DefaultRouter
from shops.views import (
    CategoryListCreateAPIView,
    ProductListCreateAPIView,
    ProductsByCategoryView,
    # OrderViewSet
    OrderListCreateAPIView, AddressListCreateAPIView, OrderListByOperatorAPIView,
)

router = DefaultRouter()
# router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('order/', OrderListCreateAPIView.as_view(), name='order'),
    path('address/', AddressListCreateAPIView.as_view(), name='address'),
    path('categories/<int:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('operators/<int:operator_id>/orders/', OrderListByOperatorAPIView.as_view(), name='operator-orders'),

]

urlpatterns += router.urls
