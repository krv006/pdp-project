from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegisterUserModelSerializer, LoginUserModelSerializer


@extend_schema(tags=['users'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Successfully registered!'
        }, status=status.HTTP_201_CREATED)


@extend_schema(tags=['users'])
class LoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    # This method should be defined for GenericAPIView to work correctly
    def get_serializer_class(self):
        return LoginUserModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # This will work now
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
