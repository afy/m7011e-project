from django.shortcuts import render

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
# Superuser views