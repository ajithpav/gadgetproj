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
    products = [
        {"id": 1, "name": "Wireless Headphones", "description": "High-quality sound with noise cancellation.", 
         "image": "https://source.unsplash.com/400x300/?headphones"},
        {"id": 2, "name": "Smartwatch", "description": "Track your fitness and notifications in style.", 
         "image": "https://source.unsplash.com/400x300/?smartwatch"},
        {"id": 3, "name": "Gaming Laptop", "description": "Powerful laptop for high-performance gaming.", 
         "image": "https://source.unsplash.com/400x300/?laptop,gaming"},
        {"id": 4, "name": "Bluetooth Speaker", "description": "Portable speaker with deep bass and long battery life.", 
         "image": "https://source.unsplash.com/400x300/?speaker"},
        {"id": 5, "name": "4K Action Camera", "description": "Capture adventures with ultra-HD clarity.", 
         "image": "https://source.unsplash.com/400x300/?camera"},
        {"id": 6, "name": "Smart Home Assistant", "description": "Control your home with voice commands.", 
         "image": "https://source.unsplash.com/400x300/?smarthome,assistant"},
    ]
    return render(request, 'shop/shop.html', {"products": products})



def collection(request):
    products = Product.objects.all()  # Ensure this query is valid
    return render(request, 'shop/collection.html', {'products': products})



def reviews(request):
    # Fetch all reviews
    reviews = Review.objects.all()
    
    # Precompute the stars for each review based on the rating
    for review in reviews:
        review.stars = '⭐' * review.rating  # Assuming rating is an integer
    
    # Render the reviews template and pass the reviews data
    return render(request, 'shop/reviews.html', {'reviews': reviews})



def about(request):
    return render(request, 'shop/about.html')
