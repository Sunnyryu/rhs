from django.urls import path
from . import views



urlpatterns = [
        path('order_result/<int:id>/', views.neworder),
        path('order_result/', views.order_result),
        path('order/', views.order),
        path('', views.index),

        ]
