from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from News.models import News, Tag
from News.serializers import NewsSerializer, TagSerializer
# Create your views here.


class NewsListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TagDetailAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
