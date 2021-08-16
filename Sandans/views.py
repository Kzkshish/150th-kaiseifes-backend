from datetime import datetime, timezone, timedelta

from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.views import LoginView

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from Sandans.models import Sandan
from Sandans.serializers import SandanSerializer
from .forms import WaittimeUpdateForm, LoginForm

JST = timezone(timedelta(hours=+9), 'JST')

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


class WaittimeUpdate(LoginRequiredMixin, UpdateView):
    template_name = "Sandans/waittime_update.html"
    login_url = "/login"
    form_class = WaittimeUpdateForm
    success_url = reverse_lazy("Sandans:waittime_update")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "待ち時間を変更しました")
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return get_object_or_404(Sandan, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alert'] = True if datetime.now(
            JST)-self.request.user.last_updated > timedelta(minutes=10) else False
        return context


class Login(LoginView):
    form_class = LoginForm
    template_name = "Sandans/login.html"

    def form_valid(self, form):
        messages.success(self.request, "ログインしました。")
        return super().form_valid(form)
