from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

User = get_user_model()


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')  # Eslatma: bu yerda qavslar kiritildi

        # Tavsiya qilinmaydi, lekin agar vaqtincha kerak bo'lsa:
        # todo bunda write_only bolganda yoziladi lekin post va get qilganda korinmaydi swaggerda
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

        # todo bunda read_only bolgani uchun faqat korsa boladi va ozgartirish kiritib bolmaydi
        # extra_kwargs = {
        #     "password": {
        #         "read_only": True,
        #     }
        # }

    def validate(self, attrs):
        password = attrs.get('password')
        if password:
            attrs['password'] = make_password(password)  # 'password' string sifatida ishlatiladi
        return super().validate(attrs)


class SendEmailSerializer(Serializer):
    email = EmailField()


class EmailModelSerializer(Serializer):
    email = EmailField(help_text='Enter email')


class VerifyModelSerializer(Serializer):
    email = EmailField(help_text='Enter email')
    code = CharField(max_length=8, help_text='Enter confirmation code')

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        cache_code = str(cache.get(email))
        if code != cache_code:
            raise ValidationError('Code not found or timed out')
        return attrs
