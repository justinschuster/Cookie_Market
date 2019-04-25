# homepage/models.py

from django.db import models

# Model for a Cookie
class Cookie(models.Model):
    # TODO: Either select what type of cookie on page or here. Don't let user submit custom name, but will decided later.
    name = models.CharField(max_length=30) 
    price = models.IntegerField()
