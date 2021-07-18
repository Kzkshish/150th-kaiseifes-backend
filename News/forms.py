from django.forms import ModelForm
from News.models import News
from django_summernote.widgets import SummernoteWidget


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ("title", "text", "tag", "is_important",)
        widgets = {
            "text": SummernoteWidget()
        }
