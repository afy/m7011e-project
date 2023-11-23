from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .gateway_client import ApiGatewayClient
import json
api_gateway_client = ApiGatewayClient()

# Create your views here.

def app(request):
    print("Entered app")
    return HttpResponse("<h>Hello world<h>")

def get_product(request, name):
    print("Entered get_product")
    response = api_gateway_client.call(name)
    
    return JsonResponse(json.loads(response.decode()))
