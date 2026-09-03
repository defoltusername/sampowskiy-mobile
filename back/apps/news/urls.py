from django.urls import path
from .views import news, news_detail

urlpatterns = [
    path("news/", news),
    path("news/<int:news_id>/", news_detail),
]
