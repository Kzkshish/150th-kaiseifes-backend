from django.urls import path
from . import views

app_name = "News"
urlpatterns = [
    path("api/news/", views.NewsListAPIView.as_view(), name="news_list"),
    path("api/news/<int:pk>",
         views.NewsDetailAPIView.as_view(), name="news_detail"),
    path("api/news/tags/<int:pk>",
         views.TagDetailAPIView.as_view(), name="tag_detail"),
    path("api/news/tags", views.TagListAPIView.as_view(), name="tag_list")
]
