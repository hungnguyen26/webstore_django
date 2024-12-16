from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('Login/', views.LoginPage, name='Login'),
    path('Search/', views.Search, name='Search'),
    path('category/', views.category, name='category'),
    path('Logout/', views.logoutPage, name='Logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
]
