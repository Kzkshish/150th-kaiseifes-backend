from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from Sandans.models import Sandan
from Sandans.serializers import SandanSerializer

# Create your views here.


class SandanListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Sandan.objects.all()
    serializer_class = SandanSerializer

    def get(self, request):
        sandan_list = [[sandan.id, sandan.username, sandan.waittime]
                       for sandan in Sandan.objects.filter(is_superuser=False)]
        ret = [{"id": sandan[0], "name":sandan[1], "waittime":sandan[2]}
               for sandan in sandan_list]
        return Response(data=ret, status=HTTP_200_OK)


class SandanWaittimeOrderAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Sandan.objects.all()

    def get(self, request):
        sandan_list = [[sandan.id, sandan.username, sandan.waittime]
                       for sandan in Sandan.objects.filter(is_superuser=False)]
        ret = [{"id": sandan[0], "name":sandan[1], "waittime":sandan[2]}
               for sandan in sorted(sandan_list, key=lambda x: x[2])]
        return Response(data=ret, status=HTTP_200_OK)
