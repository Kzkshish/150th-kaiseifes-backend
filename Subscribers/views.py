from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string

from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.serializers import ModelSerializer

from Subscribers.serializers import SubscriberSerializer, SubscriberDeleteSerializer
from Subscribers.models import Subscriber

# Create your views here.


class RegisterSubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = SubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_mail(subject="150th開成祭 メルマガ登録のお知らせ", message=render_to_string("FirstTimeMail.html"),
                  from_email="150th KaiseiFes HP", recipient_list=(request.data["email"],), html_message=render_to_string("FirstTimeMail.html"))
        return Response(serializer.data, status=HTTP_201_CREATED)


class CancelSubsclibeAPIView(DestroyAPIView):
    serializer_class = SubscriberDeleteSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        subscriber = get_object_or_404(Subscriber, email=request.data["email"])
        subscriber.delete()
        return Response(status=HTTP_204_NO_CONTENT)
