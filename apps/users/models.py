from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    email = EmailField(max_length=155, unique=True)

    def __str__(self):
        return self.email
