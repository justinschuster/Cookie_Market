# homepage/models.py

from django.contrib.auth.models import User
from django.db import models

from .choices import *


# Model for a Cookie Listing
class Cookie(models.Model):
    # TODO: Either select what type of cookie on page or here. Don't let user submit custom name, but will decided later.
    cookie_type = models.IntegerField(choices=COOKIE_CHOICES, default=1)
    price = models.IntegerField()
    # TODO: Need to add a product id system.

    def __str__(self):
        return self.cookie_type
