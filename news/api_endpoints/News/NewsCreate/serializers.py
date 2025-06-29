from news.models import News
from rest_framework import serializers

class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "content", "Author_id", "image_id", "is_active"]

        def to_representation(self, instance):
            instance = {
                "title": instance.title,
                "content": instance.content,
                "Author_id": instance.Author_id,
                "image_id": instance.image_id,
                "is_active": instance.is_active,
            }
            return instance
        
