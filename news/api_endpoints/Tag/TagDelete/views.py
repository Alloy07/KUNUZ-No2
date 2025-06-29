from rest_framework.generics import DestroyAPIView

from news.models import Tag
from news.api_endpoints.Tag.TagDelete.serializers import TagDeleteSerializer


class TagDeleteAPIView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)