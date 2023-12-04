from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
#from .APIGatewayServer import ApiGatewayServer
from .queries import *

# Create your views here.
def home(request):
    return HttpResponse("hello world")

insert_query()





