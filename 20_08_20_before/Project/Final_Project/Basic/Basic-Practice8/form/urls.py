from django.urls import path
from . import views

app_name= "form"
urlpatterns = [
        path('', views.index, name="index"),
        path('new/', views.new, name="new"),
        path('detail/', views.detail, name="detail"),


        
]
