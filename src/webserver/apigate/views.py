from django.http import JsonResponse
from rest_framework.decorators import api_view

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared.pikacomms.client import PikaClient

# Tables: Product, Special_Sale, Product_Discount, Category, User

# Communicate with microservices
api_gateway_client = PikaClient(name="API-gate-client")
print("Initialized client")

# Handle Product table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_product_crud(request, id):
    response = api_gateway_client.call("prod", "create_product", {"test":1}, None)
    return JsonResponse(response)

# Handle Category table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_category_crud(request, id):
    response = api_gateway_client.call("prod", "create_category", {"test":1}, None)
    return JsonResponse(response)

# Handle User table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_user_crud(request, id):
    response = api_gateway_client.call("auth", "create_user", {"test":1}, None)
    return JsonResponse(response)