from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Shop


def home(request):
    return render(request, 'shop/home.html')


def category(request):
    return render(request, 'shop/category.html')


def form(request):
    return render(request, 'shop/form.html')


def product(request):
    queryset = Shop.objects.all()
    return render(request, 'shop/product.html', {'queryset': queryset})

