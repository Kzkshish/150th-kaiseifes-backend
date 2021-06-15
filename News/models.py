from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.TextField()


class New(models.Model):
    created_date = models.DateField(auto_now_add=True)
    title = models.TextField()
    text = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
