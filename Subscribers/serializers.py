from rest_framework import serializers
from Subscribers.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"


class SubscriberDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ("email",)
