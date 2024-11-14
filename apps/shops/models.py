from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, ImageField, TextChoices, \
    CharField, SmallIntegerField, BooleanField, URLField, TextField
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey

from django.db.models import CharField, DateTimeField, Model, SlugField
from django.utils.text import slugify


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} - {self.updated_at}'


class Category(MPTTModel, BaseSlugModel):
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
    background_image = ImageField(upload_to='categories/')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(Model):
    class Size(TextChoices):
        F50 = '50', '50'
        F52 = '52', '52'
        F54 = '54', '54'
        F56 = '56', '56'

    class Poll(TextChoices):
        MALE = 'Male', 'male'
        FEMALE = 'Female', 'female'

    class Color(TextChoices):
        WHITE = 'White', 'white'
        RED = 'Red', 'red'
        BLUE = 'Blue', 'blue'
        GREEN = 'Green', 'green'
        YELLOW = 'Yellow', 'yellow'
        BROWN = 'Brown', 'brown'
        GREY = 'Grey', 'grey'
        SKY_BLUE = 'Sky Blue', 'sky blue'
        BLACK = 'Black', 'black'

    name = CharField(max_length=255)
    price = PositiveIntegerField(default=0)
    description = CKEditor5Field()
    discount_price = SmallIntegerField(default=0, null=True, blank=True)
    size = CharField(max_length=2, choices=Size.choices, default=Size.F50)
    poll = CharField(max_length=10, choices=Poll.choices, default=Poll.MALE)
    color = ColorField(choices=Color.choices, default=Color.WHITE)
    material = CharField(max_length=255, null=True, blank=True)
    lining = CharField(max_length=255, null=True, blank=True)  # todo podkladka
    made_from = CharField(max_length=255, null=True, blank=True)
    category = ForeignKey('shops.Category', CASCADE, related_name='products')

    # TODO discount_price mana shuni kiritganda nechi foiz sale boletganini xam chiqazib berishi kerak -> ustozdan sorimiz
    # TODO sale nechi foiz kiritganda shunda summasini ozi aftamatik olishi kerak -> ustozdan sorimiz


class Address(Model):
    class Type(TextChoices):
        HOME = 'Доставка на дом', 'доставка на дом'
        FILIAL = 'Пункт выдачи СДЭК', 'пункт выдачи СДЭК'
        RUSSIAN = 'Россия', 'pоссия'

    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    city = CharField(max_length=100)
    home_number = CharField(max_length=100)
    deliver_place = CharField(max_length=100, choices=Type.choices, default=Type.RUSSIAN)
    email = EmailField()
    phone_number = CharField(max_length=100)
    description = TextField()


class Brand(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='images/brand/')


class Payment(Model):
    name = CharField(max_length=255)
    surname = CharField(max_length=255)
    delivery_home = BooleanField(default=True)
    SDEK_pickup_point = BooleanField(default=False)
    region = CharField(max_length=255)


class Image(Model):
    image = ImageField(upload_to='images/product/')
    product = ForeignKey('shops.Product', on_delete=CASCADE, related_name='images')


class SiteSettings(Model):
    instagram = URLField()
    telegram = URLField()


class Order(TimeBaseModel):
    product = ForeignKey('shops.Product', CASCADE, related_name='orders')
    address = ForeignKey('shops.Address', CASCADE, related_name='orders')
    owner = ForeignKey('users.User', CASCADE, related_name='orders')
    payment = ForeignKey('shops.Payment', CASCADE, related_name='orders')


class QuickOrder(Model):
    name = CharField(max_length=255)
    phone_number = CharField(max_length=255)
    order = ForeignKey('shops.Product', CASCADE, related_name='quick_orders')
