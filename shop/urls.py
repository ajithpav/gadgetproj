from django.urls import path
from . import views
from .views import collection
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/', views.shop, name='shop'),
    path('collection/', collection, name='collection'),
    path('reviews/', views.reviews, name='reviews'),
    path('about/', views.about, name='about'),
]
