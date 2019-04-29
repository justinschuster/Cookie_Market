from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from .forms import CookieForm
from .models import Cookie

# Create your tests here.
class CookieFormTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('beezlebub')
        self.cookie = Cookie.objects.create(cookie_type='samoas', seller=user, price=15, post_date=timezone.now())

    def test_init(self):
        CookieForm(request.POST)

    def test_valid_data(self):
        form = CookieForm({
            'cookie_type': 'samoas',
            'seller': user,
            'price': 15,
            'post_date': timezone.now(),
        }, cookie=self.cookie)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(cookie.cookie_type, 'samoas')
        self.assertEqual(cookie.seller, user)
        self.assertEqual(cookie.price, 15)
        self.assertEqual(cookie.post_date, timezone.now())

    def test_blank_data(self):
        form = CookieForm({}, cookie=self.cookie)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'cookie_type': ['required'],
            'seller': ['required'],
            'price': ['required'],
            'post_date': ['required'],
        })
