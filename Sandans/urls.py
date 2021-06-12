from django.urls import path
from Sandans.views import SandanListAPIView

app_name = "Sandans"
urlpatterns = [
    path("api/sandans/", SandanListAPIView.as_view(), name="sandan_list")
]
