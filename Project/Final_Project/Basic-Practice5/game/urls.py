from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('game/detail/', views.detail),
        path('new/', views.new),
        path('<int:id>/newdetail/', views.newdetail),


]
