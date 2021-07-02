from django.urls import path
from Sandans.views import SandanListAPIView, SandanWaittimeOrderAPIView

app_name = "Sandans"
urlpatterns = [
    path("api/sandans", SandanListAPIView.as_view(), name="sandan_list"),
    path("api/sandans/waittime_order",
         SandanWaittimeOrderAPIView.as_view(), name="sandan_waittime_order")
]
