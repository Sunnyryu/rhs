from django.db import models

# Create your models here.
class Test(models.Model):
    date = models.CharField(max_length=200)
    value1 = models.CharField(max_length=100)
    value2 = models.CharField(max_length=100)

    def __str__(self):
        return self.value1
