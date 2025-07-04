from news.models import Category
from rest_framework import serializers

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
