from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('new/', views.new),
        path('create/', views.create),
        path('<int:pk>/example/', views.detail),
        path('<int:pk>/update/', views.update),
        path('<int:pk>/revise/', views.revise),
        path('<int:pk>/delete/', views.delete),

]
