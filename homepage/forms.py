# homepage/forms.py

from django import forms
from django.forms import ModelForm, Select

from .models import Cookie, BuyOrder
from .choices import *


class CookieForm(ModelForm):
    cookie_type = forms.ChoiceField(choices=COOKIE_CHOICES, label='', widget=Select(), required=True)

    class Meta:
        model = Cookie
        fields = ['cookie_type', 'price']
    
class BuyOrderForm(ModelForm):

    class Meta:
        model = BuyOrder
        fields = ['date_ordered']

