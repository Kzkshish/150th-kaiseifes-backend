from django.shortcuts import render, reverse
from django.views.generic import CreateView, View, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mass_mail, send_mail
from django.template.loader import render_to_string

from News.models import News
from News.forms import NewsForm

from Subscribers.models import Subscriber

# Create your views here.


class NewsCreateFormView(CreateView):
    form_class = NewsForm
    template_name = "AdminControl/post_news.html"
    success_url = reverse_lazy('AdminControl:post_news')

    def form_valid(self, form):
        news = form.save()
        messages.success(self.request, "お知らせを投稿しました。")

        for subscriber in Subscriber.objects.all():
            send_mail(news.title, news.text,
                      "150th KaiseiFes HP", (subscriber.email,), html_message=news.text)
        messages.success(self.request, "メールの送信が完了しました。")

        return HttpResponseRedirect(reverse('AdminControl:post_news'))
