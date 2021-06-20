from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
# Create your models here.


class Sandan(AbstractUser):
    icon = models.ImageField(null=True, upload_to="icons/")
    links = models.URLField(blank=True, null=True)
    books = models.FileField(
        upload_to="books/", blank=True, null=True)
    waittime = models.IntegerField(default=0)
