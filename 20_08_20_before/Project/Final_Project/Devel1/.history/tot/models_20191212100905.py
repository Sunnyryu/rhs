from django.db import models

# Create your models here.
class Keyword(models.Model):
    word = models.CharField(max_length=30)
    date = models.DateField()
    highword1 = models.CharField(max_length=30)
    frequency1 = models.CharField(max_length=30)
    highword2 = models.CharField(max_length=30)
    frequency2 = models.CharField(max_length=30)
    highword3 = models.CharField(max_length=30)
    frequency3 = models.CharField(max_length=30)
    highword4 = models.CharField(max_length=30)
    frequency4 = models.CharField(max_length=30)
    highword5 = models.CharField(max_length=30)
    frequency5 = models.CharField(max_length=30)
    highword6 = models.CharField(max_length=30)
    frequency6 = models.CharField(max_length=30)
    highword7 = models.CharField(max_length=30)
    frequency7 = models.CharField(max_length=30)
    highword8 = models.CharField(max_length=30)
    frequency8 = models.CharField(max_length=30)
    highword9 = models.CharField(max_length=30)
    frequency9 = models.CharField(max_length=30)
    highword10 = models.CharField(max_length=30)
    frequency10 = models.CharField(max_length=30)
