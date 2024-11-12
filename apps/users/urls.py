from django.urls import path
from users.views import UserListCreateAPIView, SendEmailAPIView, VerifyEmailAPIView

urlpatterns = [
    path('register/', UserListCreateAPIView.as_view(), name='register'),
    path('auth/send-email/', SendEmailAPIView.as_view(), name='send-email'),
    path('auth/verify-code/', VerifyEmailAPIView.as_view(), name='verify-email'),

]
