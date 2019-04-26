# homepage/forms.py

from django.forms import ModelForm
from .models import Cookie

class CookieForm(ModelForm):
    class Meta:
        model = Cookie
        fields = ['cookie_type', 'seller', 'price', 'post_date']
