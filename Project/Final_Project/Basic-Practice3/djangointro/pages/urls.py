from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('lotto_result/', views.lotto_result),
    path('comment/', views.comment),
    path('text/', views.text),
    path('artii_form/', views.artii_form),
    path('artii_result/', views.artii_result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('subway_add/', views.subway_add),
    path('subway_result/', views.subway_result),
    path('example/', views.example),

        ]
