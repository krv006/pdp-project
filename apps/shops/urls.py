from django.urls import path

from shops.views import CategoryListCreateAPIView, ProductListCreateAPIView, ProductsByCategoryView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('categories/<int:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),

]
