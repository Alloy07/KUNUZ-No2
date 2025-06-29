from django.contrib import admin
from news.models import News, Tag, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author_id', 'is_active', 'views_count')  # columns to show in list view
    list_filter = ('is_active',)              # filter sidebar for active status
    search_fields = ('title', 'content')     # add search box for title and content
    raw_id_fields = ('Author_id', 'image_id') # optimize foreign key fields with raw id widget
    filter_horizontal = ('liked_by',)         # better UI for many-to-many field


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


