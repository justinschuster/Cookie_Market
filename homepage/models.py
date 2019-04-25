# homepage/models.py

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Model for a Cookie Listing
class Cookie(models.Model):
    # TODO: Either select what type of cookie on page or here. Don't let user submit custom name, but will decided later.
    cookie_type = models.CharField(max_length=30) 
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    post_date = models.DateField()
    # TODO: Need to add a product id system.

    def __str__(self):
        return self.cookie_type

class CookieForm(ModelForm):
    class Meta:
        model = Cookie
        fields = ['cookie_type', 'seller', 'price', 'post_date']
