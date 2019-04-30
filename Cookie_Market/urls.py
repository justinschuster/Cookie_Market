"""Cookie_Market URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import include, path

from homepage.views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('samoas/', samoas, name='samoas'),
    path('thin_mints/', thin_mints, name='thin_mints'),
    path('tagalongs/', tagalongs, name='tagalongs'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', sign_up, name='sign_up'),
    path('sell/', sell, name='sell'),
    path('buy/<int:product_id>/', buy, name='buy'),
    path('buy/<int:oid>/thank_you/', thank_you, name='thank_you'),
]
