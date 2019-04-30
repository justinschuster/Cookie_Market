# homepage/urls.py

from django.conf.urls import include, url

from homepage.views import index, samoas

app_name = 'homepage'

urlpatterns += [
    url(r'buy/(?P<product_id>[0-9]+)/', views.buy, name='buy'),
    url(r'^thank_you/(?P<oid>[0-9]+)/', views.thank_you, name='thank_you')
]
