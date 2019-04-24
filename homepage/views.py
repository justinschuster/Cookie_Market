# homepage/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'homepage'

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def samoas(request):
    return render(request, 'samoas.html', {})
