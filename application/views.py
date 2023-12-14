from django.shortcuts import render
from django.http import HttpResponse
from .models import products

# Create your views here.
def home(request):
    productss = products.objects.all()
    return render(request, 'home.html',{'products':productss})

def new(request):
    productss = products.objects.all()
    return render(request, 'new.html',{'products':productss})

def underwear(request):
    productss = products.objects.all()
    return render(request, 'underwear.html',{'products':productss})

def sport(request):
    productss = products.objects.all()
    return render(request, 'sport.html',{'products':productss})