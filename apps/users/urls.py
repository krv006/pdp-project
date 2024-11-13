from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterCreateAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
