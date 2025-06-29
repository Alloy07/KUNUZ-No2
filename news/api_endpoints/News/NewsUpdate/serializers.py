from news.models import News
from rest_framework import serializers

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "content"]