# homepage/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .choices import *


# Model for a Cookie Listing
class Cookie(models.Model):
   
    cookie_id =  models.AutoField(primary_key=True)

    cookie_type = models.IntegerField(choices=COOKIE_CHOICES, default=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.IntegerField()
    

    def __str__(self):
        return str(self.cookie_id)
        
class BuyOrder(models.Model):
    date_ordered = models.DateTimeField(default=timezone.now)
    
    cookie_id = models.ForeignKey(Cookie, blank=False, null=False, on_delete=models.CASCADE)

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
