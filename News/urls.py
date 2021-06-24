from django.urls import path
from . import views

app_name = "News"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('tag/<str:tag>/', views.tag, name ='tag'),
    path('detail/<int:news_id/', views.detail, name = 'detail')
    ]