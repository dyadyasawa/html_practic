
from django.contrib import admin

from users.models import User, Message


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
    )
    list_filter = ("email",)
    search_fields = ("email",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "addressee",
        "message",
    )
    list_filter = ("addressee",)
    search_fields = ("addressee",)
