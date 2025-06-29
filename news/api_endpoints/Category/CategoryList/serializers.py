from news.models import Category
from rest_framework import serializers

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( "name", "slug", "news_ids")

