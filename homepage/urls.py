# homepage/urls.py

from django.conf.urls import include, url

from homepage.views import index, samoas

app_name = 'homepage'

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^samoas/$', samoas, name='samoas'),
]
