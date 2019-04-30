# homepage/admin.py

from django.contrib import admin

from .models import Cookie, BuyOrder

admin.site.register(Cookie)
admin.site.register(BuyOrder)
