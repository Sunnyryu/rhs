from django.db import models

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
