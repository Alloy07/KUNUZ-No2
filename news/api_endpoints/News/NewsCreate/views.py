from rest_framework.generics import CreateAPIView

from news.models import News
from news.api_endpoints.News.NewsCreate.serializers import NewsCreateSerializer


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    