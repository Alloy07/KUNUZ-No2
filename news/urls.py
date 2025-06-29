from django.urls import path

from news.api_endpoints.Tag import (
    TagCreateAPIView,
    TagDeleteAPIView,
    TagsUpdateAPIView,
    TagListAPIView,
)
from news.api_endpoints.Category import (
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryUpdateAPIView,
    CategoryListAPIView,
)


urlpatterns = [
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagsUpdateAPIView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteAPIView.as_view(), name='tag-delete'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),
]