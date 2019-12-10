from django.urls import path
from . import views

app_name="movie"
urlpatterns = [
        path('movie/', views.movie, name='movie'),
        path('new/', views.new, name='new'),
        path('<int:movie_id>', views.detail, name='detail'),
        path('<int:movie_id>/edit', views.edit, name='edit'),
        path('<int:movie_id>/delete', views.delete, name='delete'),



]
