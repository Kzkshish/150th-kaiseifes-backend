from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from Sandans.models import Sandan
from Sandans.serializer import SandanSerializer

# Create your views here.


class SandanListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Sandan.objects.all()
    serializer_class = SandanSerializer
