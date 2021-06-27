from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

from News.models import News
from News.forms import NewsForm

# Create your views here.


class NewsCreateFormView(CreateView):
    form_class = NewsForm
    template_name = "AdminControl/post_news.html"
    success_url = reverse_lazy('AdminControl:post_news')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "お知らせを投稿しました。")
        # メールを送信
        return HttpResponseRedirect(reverse('AdminControl:post_news'))
