# homepage/models.py

from django.db import models

# Model for a Cookie Listing
class Cookie(models.Model):
    # TODO: Either select what type of cookie on page or here. Don't let user submit custom name, but will decided later.
    cookie_type = models.CharField(max_length=30) 
    seller = models.CharField(max_length=30)
    price = models.IntegerField()
    post_date = models.DateField()

    def __str__(self):
        return self.cookie_type
