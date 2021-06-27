from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from Subscribers.serializers import SubscriberSerializer
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
        return Response(serializer.data, status=HTTP_201_CREATED)


class CancelSubsclibeAPIView(DestroyAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        subscriber = get_object_or_404(Subscriber, email=request.data["email"])
        subscriber.delete()
        return Response(status=HTTP_204_NO_CONTENT)
