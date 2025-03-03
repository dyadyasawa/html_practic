
from django.contrib import admin

from cars.models import Car, Category


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "price",
    )
    list_filter = ("price",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",

    )
    list_filter = ("name",)
    search_fields = ("name",)


# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = (
#         "addressee",
#         "message",
#     )
#     list_filter = ("addressee",)
#     search_fields = ("addressee",)
