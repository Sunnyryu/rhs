"""djangointro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('util/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    #path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    #path('throw/', views.throw),
    #path('catch/', views.catch),
    #path('lotto/', views.lotto),
    #path('lotto_result/', views.lotto_result),
    #path('comment/', views.comment),
    #path('text/', views.text),
    #path('artii_form/', views.artii_form),
    #path('artii_result/', views.artii_result),
    #path('user_new/', views.user_new),
    #path('user_create/', views.user_create),
    #path('subway_add/', views.subway_add),
    #path('subway_result/', views.subway_result),
    #path('example/', views.example),
    ]
