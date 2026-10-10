from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})

# Create your views here.
