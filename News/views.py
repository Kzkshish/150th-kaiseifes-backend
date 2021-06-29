from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from News.models import News, Tag
from News.serializers import NewsSerializer
# Create your views here.


def index(request):
    news = News.objects.order_by('created_datetime')
    return render(request, 'News/index.html', {'news': news})


def tag(request, tag):
    tags = Tag.objects.get(name=tag)
    news = News.objects.filter(tag=tag)
    return render(request, 'News/index.html', {'tag': tags, 'news': news})


def detail(request, news_id):
    news = News.objects.order_by('created_datetime')
    return render(request, 'News/index.html', {'news': news})


class NewsListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        news_dict = {
            "title": news.title,
            "text": news.text,
            "datetime": news.datetime,
            "tag": [tag.id for tag in news.tag.all()]
        }
        return Response(data=news_dict, status=HTTP_200_OK)
