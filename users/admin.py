from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_admin")
    list_filter = ("email", "is_admin")
    fieldsets = (
        (None, {"fields": ("email", "password",)}),
        ("Permissions", {"fields": ("is_admin",)}),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["is_active", "date_joined"],
            },
        ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2")
        }
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
    
