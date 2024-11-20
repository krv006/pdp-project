from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterCreateAPIView, LoginAPIView, UserListAPIView, OperatorListCreateAPIView, \
    OperatorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('operators/', OperatorListCreateAPIView.as_view(), name='operator-list-create'),
    path('operators/<int:pk>/', OperatorRetrieveUpdateDestroyAPIView.as_view(), name='operator-detail'),

]
