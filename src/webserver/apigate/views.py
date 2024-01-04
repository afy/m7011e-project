from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

#from ...shared.pikacomms.client import PikaClient

#api_gateway_client = PikaClient()

def app(request):
    print("Entered app")
    return HttpResponse("<h>Hello world<h>")

def get_product(request, name):
    print("Entered get_product")
    #response = api_gateway_client.call(name)
    response = {}
    return JsonResponse(response)