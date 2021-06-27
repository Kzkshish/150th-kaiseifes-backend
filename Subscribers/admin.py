from django.contrib import admin

from Subscribers.models import Subscriber

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    model = Subscriber
    list_display = ["email"]


admin.site.register(Subscriber, SubscriberAdmin)
