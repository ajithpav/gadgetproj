#Gadget_Ecomerse website

# E-Commerce Shop

## Overview
This is a Django-based e-commerce web application that allows users to browse products, track orders, submit reviews, and contact support. It includes various sections such as home, shop, product details, collections, reviews, and more.

## Features
- **Home Page**: Displays featured products.
- **Shop Page**: Lists available products with details and images.
- **Product Details**: View detailed product descriptions and customer reviews.
- **Order Tracking**: Simulated order tracking system using AWB number, order ID, and mobile number.
- **Contact Form**: Users can submit inquiries via a form, which sends emails to the admin.
- **Customer Reviews**: Users can read and view ratings for products.
- **Collections**: Displays all available products.
- **Category Pages**: Includes sections for Couples Cases, Anime Cases, and Marvel Cases.

## Installation
### Prerequisites
- Python 3.x
- Django
- pip

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-shop.git
   cd ecommerce-shop
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure
```
shop/
│── migrations/         # Database migrations
│── static/             # Static files (CSS, JS, images)
│── templates/shop/     # HTML templates
│── models.py           # Database models (Product, Review)
│── views.py            # Application views (Logic for rendering pages)
│── urls.py             # URL patterns
│── forms.py            # Django forms (Contact Form)
│── admin.py            # Django Admin configurations
│── settings.py         # Django settings
```

## Routes & Views
| Route | View Function | Description |
|--------|-------------|-------------|
| `/` | `home` | Displays featured products on the home page. |
| `/shop/` | `shop` | Lists available products with descriptions. |
| `/product/<id>/` | `product_detail` | Shows detailed product information and reviews. |
| `/track-order/` | `track_order` | Simulated order tracking with AWB number and order ID. |
| `/contact/` | `contact` | Contact form to send inquiries via email. |
| `/reviews/` | `reviews` | Displays all customer reviews. |
| `/collection/` | `collection` | Shows a collection of available products. |
| `/couples-case/` | `couples_case` | Displays couples' cases products. |
| `/anime-case/` | `anime_case` | Displays anime-themed cases. |
| `/marvel-case/` | `marvel_case` | Displays Marvel-themed cases. |

## Contact
For any queries, reach out to us at: ajithkumar63073@gmail.com`

---

### License
This project is licensed under the MIT License. Feel free to modify and use it for your needs.
