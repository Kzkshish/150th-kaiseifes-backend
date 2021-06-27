from django.forms import ModelForm
from News.models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ("title", "text", "tag",)
