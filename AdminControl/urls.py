from django.urls import path

from AdminControl.views import NewsCreateFormView

app_name = "AdminControl"
urlpatterns = [
    path("admincontrol/postnews", NewsCreateFormView.as_view(), name="post_news")
]
