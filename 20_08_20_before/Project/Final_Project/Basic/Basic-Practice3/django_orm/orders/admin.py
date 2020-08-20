from django.contrib import admin
from .models import Subway
# Register your models here.

class SubwayAdmin(admin.ModelAdmin):
    fields = ['name', 'datetime', 'sandwitch', 'size', 'bread', 'check' ]
    list_filter = ['name'] 
    search_fields = ['name', 'datetime']

admin.site.register(Subway, SubwayAdmin)
