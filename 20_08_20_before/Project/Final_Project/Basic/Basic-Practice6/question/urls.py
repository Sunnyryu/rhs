from django.urls import path
from . import views

app_name= "question"
urlpatterns = [
        path('', views.index, name='index'),
        path('new/', views.new, name="new"),
        path('<int:que_id>', views.detail, name="detail"),
        path('<int:que_id>/edit/', views.edit, name="edit"),
        path('<int:que_id>/delete/', views.delete, name="delete"),
        path('<int:que_id>/survey/', views.survey, name="survey"),
        path('<int:c_id>/survey_edit/', views.survey_edit, name="survey_edit"),
        path('<int:c_id>/survey_delete/', views.survey_del, name="sur_del"),
        path('<int:c_id>/vote/', views.vote, name="vote"),
        ]
