# homepage/urls.py

from django.conf.urls import url
from homepage import views

urlpatterns = [
        url('', views.HomePageView.as_view()),
]
