from news.models import Tag
from rest_framework import serializers

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("news_ids", "name", "slug")

