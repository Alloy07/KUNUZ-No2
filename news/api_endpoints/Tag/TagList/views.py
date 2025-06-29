from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from news.models import Tag
from news.api_endpoints.Tag.TagList.serializers import (
    TagListSerializer
)  



class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][TagListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class TagRetrieveAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][TagRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)