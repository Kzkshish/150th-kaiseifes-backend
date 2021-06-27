from django.urls import path
from Subscribers.views import RegisterSubscribeAPIView, CancelSubsclibeAPIView

app_name = "Subscribers"
urlpatterns = [
    path("api/subscribe/register",
         RegisterSubscribeAPIView.as_view(), name="register_subscribe"),
    path("api/subscribe/cancel", CancelSubsclibeAPIView.as_view(),
         name="cancel_subscribe")
]
