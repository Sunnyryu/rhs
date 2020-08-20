from django.contrib import admin

from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "updated_at"]
    
admin.site.register(Form, FormAdmin)
