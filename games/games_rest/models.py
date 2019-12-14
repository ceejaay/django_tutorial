from django.db import models
import datetime
from django.utils import timezone

class Games(models.Model):
    title = models.CharField(max_length=200)
    year_released = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    favorite = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

# Create your models here.
