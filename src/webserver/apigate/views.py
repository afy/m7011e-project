from django.http import JsonResponse
from rest_framework.decorators import api_view

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared.pikacomms.client import PikaClient

# Communicate with microservices
api_gateway_client = PikaClient(name="API-gate-client")
print("Initialized client")

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_product_crud(request, id):
    response = {"type":request.method, "data":request.data, "id":id}
    api_gateway_client.call("prod", "create_product", {"id": 1}, None)
    return JsonResponse(response)