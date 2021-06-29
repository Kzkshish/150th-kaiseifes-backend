from django.db import models

# Create your models here.

# created_datetimeはこのままでいいのか？編集可能にした方がいいか？

class Tag(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(blank = False, null = False, max_length = 20)
    text = models.TextField(blank = True)
    datetime = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title