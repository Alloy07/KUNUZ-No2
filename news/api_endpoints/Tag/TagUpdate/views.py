from rest_framework.generics import UpdateAPIView

from news.models import Tag
from news.api_endpoints.Tag.TagUpdate.serializers import TagsUpdateSerializer


class TagsUpdateAPIView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsUpdateSerializer