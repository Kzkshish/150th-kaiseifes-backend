from django.db import models

# Create your models here.

#あとでタグ機能を作る
class News(models.Model):
    title = models.CharField(blank = False, null = False, max_length=20)
    text = models.TextField
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title