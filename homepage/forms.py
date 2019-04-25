# homepage/forms.py

from django import forms
from homepage.models import Cookie

class ListingForm(forms.Form):
    cookie_type = forms.CharField(label='Type of cookie', max_length=15)

    class Meta:
        model = Cookie
        fields = ['cookie_type', 'seller', 'price', 'post_date']


