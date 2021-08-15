from django.urls import path
from Sandans.views import SandanListAPIView, SandanWaittimeOrderAPIView, WaittimeUpdate, Login

app_name = "Sandans"
urlpatterns = [
    path("api/sandans", SandanListAPIView.as_view(), name="sandan_list"),
    path("api/sandans/waittime_order",
         SandanWaittimeOrderAPIView.as_view(), name="sandan_waittime_order"),
    path("sandans/waittime_update",
         WaittimeUpdate.as_view(), name="waittime_update"),
    path("login", Login.as_view(), name="login"),
]
