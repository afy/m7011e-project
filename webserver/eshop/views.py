from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Homepage view")

def product(request):
    return HttpResponse("Product view")

def search(request):
    return HttpResponse("Search page")

def login(request):
    return HttpResponse("Login page")

def account(request):
    return HttpResponse("Account settings")

def cart(request):
    return HttpResponse("Cart page")

def order(request):
    return HttpResponse("Order page")