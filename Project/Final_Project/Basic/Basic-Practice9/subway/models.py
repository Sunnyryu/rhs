from django.db import models
from django.urls import reverse

class Subway(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    menu = models.CharField(max_length=10)
    bread = models.CharField(max_length=10)
    vegetable = models.CharField(max_length=30)
    sauce = models.CharField(max_length=50)
    drink = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('subway_detail', args={self.id})
# Create your models here.
