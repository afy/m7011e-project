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
#api_gateway_client = PikaClient()

def handle_product_api(request, name, func):
    #response = api_gateway_client.call(name)
    print(func)
    response = {}
    return JsonResponse(response)

def handle_auth_api(request, name, func):
    pass

def handle_order_api(request, name, func):
    pass