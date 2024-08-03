
from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "price",
    )
    list_filter = ("price",)
    search_fields = ("name",)
