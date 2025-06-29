from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from news.models import News
from news.api_endpoints.News.NewsList.serializers import (
    NewsListSerializer
)  



 

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][NewsListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][NewsRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)