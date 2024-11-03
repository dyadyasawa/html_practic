# Generated by Django 4.2.2 on 2024-08-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_category_car_carrying_car_passengers_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="category/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="car/", verbose_name="Изображение"
            ),
        ),
    ]
