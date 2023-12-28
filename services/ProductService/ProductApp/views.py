from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
#from .APIGatewayServer import ApiGatewayServer
from .queries import *


lookup = {
    "get_event":{
        "func": event_Insert_Query,
        "groups":["admin"],
        "required_fields":[("id", int),("category", str)]
    }
}

# Create your views here.
def home(request):
    return HttpResponse("hello world")





