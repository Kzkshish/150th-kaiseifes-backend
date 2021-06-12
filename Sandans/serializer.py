from rest_framework import serializers
from Sandans.models import Sandan


class SandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandan
        fields = ("username", "icon", "links", "books", "waittime")
