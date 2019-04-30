# homepage/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import CookieForm, BuyOrderForm
from .models import Cookie, BuyOrder

app_name = 'homepage'

# Create your views here.
def index(request):
    listings = Cookie.objects.all().order_by('price')
    context = {'listings': listings}

    return render(request, 'index.html', context)

def samoas(request):    
    listings = Cookie.objects.filter(cookie_type=1).order_by('price')
    context = {'listings': listings}

    return render(request, 'samoas.html', context)

def thin_mints(request):
    listings = Cookie.objects.filter(cookie_type=3).order_by('price')
    context = {'listings': listings}

    return render(request, 'thin_mints.html', context)

def tagalongs(request):
    listings = Cookie.objects.filter(cookie_type=2).order_by('price')
    context = {'listings': listings}


    return render(request, 'tagalongs.html', context)

def sell(request): 
    if request.method == 'POST':
        form = CookieForm(request.POST) 
        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('index')
    else:
        form = CookieForm()

    return render(request, 'sell.html', {'form': form})

def buy(request, product_id):
    cookie = Cookie.objects.filter(cookie_id=product_id).first()

    if request.method == 'POST':
        form = BuyOrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.buyer = request.user
            obj.product = cookie
            obj.purchase_price = cookie.price
            
            cookie.sold = True

            cookie.save()
            obj.save()
            return redirect('index')
    else:
        form = BuyOrderForm()

    return render(request, 'buy.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
