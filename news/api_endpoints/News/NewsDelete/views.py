from rest_framework.generics import DestroyAPIView

from news.models import News
from news.api_endpoints.News.NewsDelete.serializers import NewsDeleteSerializer


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)