from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid
# Create your models here.


class Sandan(AbstractUser):
    id = models.CharField(primary_key=True, max_length=5)
    icon = models.ImageField(null=True)
    links = ArrayField(base_field=models.URLField(), blank=True, null=True)
    books = ArrayField(base_field=models.FileField(), blank=True, null=True)
    waittime = models.IntegerField(default=0)
