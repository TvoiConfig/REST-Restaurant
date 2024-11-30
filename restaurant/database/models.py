from django.db import models
from django.contrib.auth.models import User

class Dishes(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    name = models.CharField(max_length=100, verbose_name="Наименования")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        db_table = 'dishes'
        verbose_name='Блюдо'
        verbose_name_plural="Блюда"

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name="Пользователь"
    )
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    latitude = models.FloatField(blank=True, null=True, verbose_name="Широта")
    longitude = models.FloatField(blank=True, null=True, verbose_name="Долгота")

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f"{self.user} {self.city} {self.street} {self.house_number}"

class Restaurant(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    city = models.CharField(max_length=100, verbose_name="Город")
    latitude = models.FloatField(blank=True, null=True, verbose_name="Широта")
    longitude = models.FloatField(blank=True, null=True, verbose_name="Долгота")

    class Meta:
        db_table = 'restaurant'
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return f"{self.address} {self.city}"

class Orders(models.Model):

    DELIVERY_CHOICES = [
        ('delivery', 'Доставка'),
        ('pickup', 'В ресторане'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Заказчик"
    )
    Dishes = models.ManyToManyField(Dishes, verbose_name="Корзина")
    delivery_type = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        default='delivery',
        verbose_name="Тип доставки"
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name = "Адрес"
    )
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name = "Ресторан"
    )

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.user} {self.delivery_type}"