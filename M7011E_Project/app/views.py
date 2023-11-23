from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def app(request):
    return HttpResponse("Hello world!")