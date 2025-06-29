from news.models import Tag
from rest_framework import serializers

class TagDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "slug", "news_ids")