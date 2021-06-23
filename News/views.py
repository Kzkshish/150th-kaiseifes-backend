from django.shortcuts import render
from .models import News
# Create your views here.

def index(request):
    news = News.objects.order_by('created_datetime')
    return render(request, 'News/index.html', {'news': news})