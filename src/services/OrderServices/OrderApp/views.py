from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .APIGatewayServer import ApiGatewayServer
from .queries import *

# Create your views here.

def home(request):
    return 0
