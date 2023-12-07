from django.shortcuts import render
import requests

# User views
def home(request):
    return render(request, 'pages/user/home.html')

def product(request):
    return render(request, 'pages/user/product.html')

def search(request):
    return render(request, 'pages/user/search.html')

def login(request):
    return render(request, 'pages/user/login.html')

def account(request):
    return render(request, 'pages/user/account.html')

def cart(request):
    return render(request, 'pages/user/cart.html')

def order(request):
    return render(request, 'pages/user/order.html')



# Admin views
def admin_home(request):
    return render(request, 'pages/admin/home.html')

def admin_orders(request):
    return render(request, 'pages/admin/orders.html')

def admin_products(request):
    return render(request, 'pages/admin/products.html')

def admin_reviews(request):
    return render(request, 'pages/admin/reviews.html')

def admin_users(request):
    return render(request, 'pages/admin/users.html')



# Superuser views
def superuser_home(request):
    return render(request, 'pages/superuser/home.html')