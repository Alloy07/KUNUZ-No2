from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    Author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    Category_ids = models.CharField(max_length=100, null=True, blank=True)
    Tags_ids = models.CharField(max_length=100, null=True, blank=True)
    Default_image = models.ImageField(upload_to="news_images", null=True, blank=True)
    image_id = models.ForeignKey('common.MediaFile', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_news', blank=True)
   
    def __str__(self):

        return self.title

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")


class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    news_ids = models.ManyToManyField(News, related_name='categories', blank=True)

    def __str__(self):
        return self.name
    
class Tag(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    news_ids = models.ManyToManyField(News, related_name='tags', blank=True)
    
    def __str__(self):
        return self.name
    