from django.db import models
from datetime import date

#Create your models here.

class Subway(models.Model):
    name = models.CharField(max_length=20)
    datetime = models.DateField(default=date.today)
    sandwitch = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    bread = models.CharField(max_length=20)
    check = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}'
