from django.urls import path
from . import views
from .views import collection
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('reviews/', views.reviews, name='reviews'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('track-order/', views.track_order, name='track_order'),
    path('collection/couple-case/', views.couples_case, name='couple-case'),
    path('collection/anime-case/', views.anime_case, name='anime-case'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('collection/marvel-case/', views.marvel_case, name='marvel-case'),
    path('collection/cartoon/',views.cartoon,name='cartoon'),

]
