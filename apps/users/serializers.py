from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_active', 'email', ]


# Register serializer
class RegisterUserModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


# Login serializer
class LoginUserModelSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise ValidationError("Invalid email or password")

        if not user.check_password(password):
            raise ValidationError("Invalid email or password")

        attrs['user'] = user
        return attrs
