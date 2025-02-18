from django.shortcuts import render
from .models import Product, Review
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse
from .forms import ContactForm

# Simulate order tracking
def track_order(request):
    tracking_info = None
    error_message = None

    if request.method == 'POST':
        awb_number = request.POST.get('awb_number')
        order_id = request.POST.get('order_id')
        mobile_number = request.POST.get('mobile_number')

        # Simulate a check for the order (this could be a database query in the real world)
        if awb_number and order_id and mobile_number:
            # For now, just simulate successful tracking info
            tracking_info = {
                'awb_number': awb_number,
                'order_id': order_id,
                'status': 'Shipped',
                'estimated_delivery_date': '2025-02-20'
            }
        else:
            error_message = "Please provide all the required details."

    return render(request, 'shop/track_order.html', {
        'tracking_info': tracking_info,
        'error_message': error_message
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extracting form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            comments = form.cleaned_data['comments']

            # Send email to admin or store it as needed
            subject = f"New Contact Form Submission from {name}"
            message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nComments:\n{comments}"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # Admin email to receive the message
                fail_silently=False,
            )
            # Optionally redirect or show a success message
            return redirect('contact_success')  # Add a URL for success page
    else:
        form = ContactForm()

    return render(request, 'shop/contact.html', {'form': form})


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

def couples_case(request):
    return render(request, 'shop/couples.html')

def anime_case(request):
    return render(request, 'shop/anime_case.html')