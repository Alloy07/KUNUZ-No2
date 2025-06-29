from news.models import News
from rest_framework import serializers

class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "content" "category", "tags", "image"]