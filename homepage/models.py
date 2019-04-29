# homepage/models.py

from django.contrib.auth.models import User
from django.db import models

from .choices import *


# Model for a Cookie Listing
class Cookie(models.Model):
    # TODO: Either select what type of cookie on page or here. Don't let user submit custom name, but will decided later.
    cookie_id =  models.AutoField(primary_key=True)
    cookie_type = models.IntegerField(choices=COOKIE_CHOICES, default=1)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    # TODO: Need to add a product id system.

    def __str__(self):
        return str(self.cookie_id)
        
