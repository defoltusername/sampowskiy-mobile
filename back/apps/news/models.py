from django.db import models


class News(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30)
    short_description = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
