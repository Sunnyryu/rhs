from django.db import models
from datetime import date

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=77)
    title_en = models.CharField(max_length=77)
    audience = models.IntegerField(default=0)
    open_date = models.DateField(default=date.today)
    genre = models.CharField(max_length=77)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField(default=0)
    post = models.TextField()
    description = models.TextField()
    def __str__(self):
        return f'{self.id} {self.title}'

