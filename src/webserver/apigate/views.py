from django.http import HttpResponse, JsonResponse

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared.pikacomms.client import PikaClient

# Routing key lookup
ms_routing = {
    "prod/": "prod",
    "order/": "order",
    "auth/": "auth",
}

# Communicate with microservices
api_gateway_client = PikaClient()

def app(request):
    print("Entered app")
    return HttpResponse("<h>Hello world<h>")

def handle_product_api(request, name):
    print("Entered get_product")
    #response = api_gateway_client.call(name)
    response = {}
    return JsonResponse(response)