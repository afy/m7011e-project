from django.shortcuts import render, redirect
import requests



# Misc
def login(request):
    if request.method == "POST":
        """
        email = request.POST.get('email')
        password = request.POST.get('password')

        response = requests.post('https://127.0.0.1:8000/api/v1/user', data=[email, password])
        token = response['Token']
        group = response['Group']

        return redirect('pages/' + group  + '/home.html', token=token, group=group)

        
        """

    
    return render(request, 'pages/login.html')


def createAccount(request):
    """
        if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        response = requests.post('https://127.0.0.1:8000/api/v1/user', data={"email":email, "username":username, "password":password})
        token = response['Token']
        group = response['Group']

        return redirect('pages/' + group  + '/home.html', token=token, group=group)
    """

    
    return render(request, 'pages/create_acc.html')



# User views
def home(request):
    return render(request, 'pages/user/home.html')

def product(request):
    return render(request, 'pages/user/product.html')

def search(request):
    return render(request, 'pages/user/search.html')


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