# homepage/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

app_name = 'homepage'

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def samoas(request):
    return render(request, 'samoas.html', {})

def thin_mints(request):
    return render(request, 'thin_mints.html', {})

def tagalongs(request):
    return render(request, 'tagalongs.html', {})

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
