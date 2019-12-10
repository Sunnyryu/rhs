from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

app_name='tot'

urlpatterns = [
    path('', views.index, name='index'),
    path('graph/', views.graph, name='graph')
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
