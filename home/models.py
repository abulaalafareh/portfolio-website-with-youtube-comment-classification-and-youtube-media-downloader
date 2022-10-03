from statistics import mode
from django.db import models

# Create your models here.

class contactme(models.Model):
    email =models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    message = models.TextField()
    Date = models.DateField()
    

class sentiment(models.Model):
    sentence = models.TextField()
    Sentiment = models.CharField(max_length=30)
    def __str__(self):
        return self.Sentiment


class downloads(models.Model):
    url =models.TextField()
    start_time = models.CharField(max_length=12)
    end_time = models.CharField(max_length=12)
    type = models.CharField(max_length=30)
    Date = models.DateField()