# homepage/urls.py

from django.urls import path 
from homepage import views

app_name = 'homepage'

urlpatterns = [
        path('', views.index, name='index'),
        path('samoas/', views.samoas, name='samoas'),
]
