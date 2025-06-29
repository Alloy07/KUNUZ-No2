from rest_framework.generics import DestroyAPIView

from news.models import Category
from news.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)