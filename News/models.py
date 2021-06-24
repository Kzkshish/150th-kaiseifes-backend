from django.db import models

# Create your models here.

#あとでタグ機能を作る

class Tag(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(blank = False, null = False, max_length = 20)
    text = models.TextField(blank = True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title