import os
import datetime
import smtplib
import ssl
import sys
import codecs
from email.mime.text import MIMEText
from dotenv import load_dotenv

from django.shortcuts import render, reverse
from django.views.generic import CreateView, View, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

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

        load_dotenv(verbose=True)
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        gmail_account = "keigo0827511@gmail.com"
        gmail_password = os.environ["MY_GMAIL_PASSWORD"]
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

        for subscriber in Subscriber.objects.all():
            msg = MIMEText(news.text, "html")
            msg["Subject"] = news.title
            msg["To"] = subscriber.email
            msg["From"] = "150th KaiseiFes HP"
            server = smtplib.SMTP_SSL(
                "smtp.gmail.com", 465, context=ssl.create_default_context())
            server.login(gmail_account, gmail_password)
            server.send_message(msg)
        messages.success(self.request, "メールの送信が完了しました。")

        return HttpResponseRedirect(reverse('AdminControl:post_news'))


"""
class NewsSendEmailView(DetailView):
    form_class = NewsForm
    template_name = "AdminControl/send_mail.html"
    success_url = reverse_lazy('AdminControl:post_news')

    def form_valid(self, form):
        print(form.data)
        return HttpResponseRedirect(reverse('AdminControl:send_mail'))
"""
