from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import User
from django.contrib import admin



admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Dashboard"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_confirmed",
    )
    list_display_links = ("id", "email", "first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Personal info"),
            {"fields": ("first_name", "last_name", "avatar", "bio")},
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_confirmed",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )