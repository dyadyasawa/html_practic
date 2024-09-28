
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """ Модель Category. """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Car(models.Model):
    """ Модель Car. """

    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE, verbose_name="Категория")
    image = models.ImageField(upload_to='car/', verbose_name='Изображение', **NULLABLE)
    year = models.DateField(verbose_name="Год выпуска")
    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    carrying = models.PositiveIntegerField(verbose_name="Грузоподъемность", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата изменения')
    passengers_count = models.PositiveIntegerField(verbose_name="Количество пассажиров без водителя", **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'Машина: {self.name}, год выпуска: {self.year}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
