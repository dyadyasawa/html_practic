# Generated by Django 4.2.2 on 2024-08-03 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="car",
            name="carrying",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Грузоподъемность"
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="passengers_count",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Количество пассажиров без водителя"
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cars.category",
                verbose_name="Категория",
            ),
        ),
    ]
