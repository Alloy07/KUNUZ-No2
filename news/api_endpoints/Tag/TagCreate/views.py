from rest_framework.generics import CreateAPIView

from news.models import Tag
from news.api_endpoints.Tag.TagCreate.serializers import TagCreateSerializer


class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    