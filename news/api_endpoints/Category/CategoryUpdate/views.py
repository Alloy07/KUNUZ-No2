from rest_framework.generics import UpdateAPIView

from news.models import Category
from news.api_endpoints.Category.CategoryUpdate.serializers import CategoryUpdateSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer