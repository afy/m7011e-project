from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

#from ...shared.pikacomms.client import PikaClient

# Load routing data from config
routing = {}
with open('../config/api-routing.json', 'r') as f:
    routing = json.loads(f.read())

#api_gateway_client = PikaClient()

def app(request):
    print("Entered app")
    return HttpResponse("<h>Hello world<h>")

def get_product(request, name):
    print("Entered get_product")
    #response = api_gateway_client.call(name)
    response = {}
    return JsonResponse(response)