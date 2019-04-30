# homepage/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import CookieForm
from .models import Cookie

app_name = 'homepage'

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def samoas(request):    
    listings = Cookie.objects.filter(cookie_type=1)
    context = {'listings': listings}

    return render(request, 'samoas.html', context)

def thin_mints(request):
    return render(request, 'thin_mints.html', {})

def tagalongs(request):
    return render(request, 'tagalongs.html', {})

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
