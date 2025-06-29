from news.models import Category
from rest_framework import serializers

class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("news_ids", "name", "slug")