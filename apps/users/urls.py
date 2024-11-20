from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterCreateAPIView, LoginAPIView, UserListAPIView

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),

]
