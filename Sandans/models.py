from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
# Create your models here.


class Sandan(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icon = models.ImageField(null=False, blank=False, upload_to="icons/")
    waittime = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)


class OnlineSandan(models.Model):
    icon = models.ImageField(null=True, upload_to="icons/")
    links = models.URLField(blank=True, null=True)
    books = models.FileField(
        upload_to="books/", blank=True, null=True)
    description = models.TextField()
