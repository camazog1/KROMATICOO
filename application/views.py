from django.shortcuts import render,get_object_or_404,redirect
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

def product(request, ref):
    product = get_object_or_404(products, ref=ref)
    productss = products.objects.all()
    return render(request, 'product.html', {'product': product, 'products':productss})