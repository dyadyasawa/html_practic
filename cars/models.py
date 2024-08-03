
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Car(models.Model):
    """ Модель Car. """

    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    year = models.DateTimeField(verbose_name="Год выпуска")
    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата изменения')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создатель')

    def __str__(self):
        return f'Машина: {self.name}, год выпуска: {self.year}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
