from django.shortcuts import render
from .models import News, Tag
# Create your views here.

def index(request):
    news = News.objects.order_by('created_datetime')
    return render(request, 'News/index.html', {'news': news})

def tag(request, tag):
    tags = Tag.objects.get(name = tag)
    news = News.objects.filter(tag = tag)
    return render(request, 'News/index.html', {'tag': tags, 'news': news})

def detail(request, news_id):
    news = News.objects.order_by('created_datetime')
    return render(request, 'News/index.html', {'news': news})
