from django.contrib import admin
from news.models import News, Tag, Category

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ("name", "slug")
    search_fields = ("name", "slug")
