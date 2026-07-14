from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "id",
        "username",
        "is_superuser",
        "is_staff",
        "is_active",
        "created_at",
        "updated_at",
    )

    ordering = ("id",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )