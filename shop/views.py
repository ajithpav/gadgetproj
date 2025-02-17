from django.shortcuts import render
from .models import Product, Review
from django.shortcuts import render

def home(request):
    featured_products = Product.objects.all()[:5]
    return render(request, 'shop/home.html', {'featured_products': featured_products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})
