from django.http import JsonResponse
from rest_framework.decorators import api_view

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared.pikacomms.client import PikaClient
from shared.pikacomms import protocol

# Tables: Product, Special_Sale, Product_Discount, Category, User

# Communicate with microservices
api_gateway_client = PikaClient(name="API Gateway", log_params=True, timeout=5)

# Handle Product table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_product_crud(request, id):
    match(request.method):
        case    "GET": response = api_gateway_client.call("prod", "get-product",
                                                           {"id": id}, 
                                                           None, None)
        case   "POST": response = api_gateway_client.call("prod", "update-product", 
                                                           {"id": id, "post-data": request.data}, 
                                                           None, None)
        case    "PUT": response = api_gateway_client.call("prod", "create-product",
                                                           {"id":id, "put-data": request.data}, 
                                                           None, None)
        case "DELETE": response = api_gateway_client.call("prod", "delete-product", 
                                                           {"product_id":id}, 
                                                           None, None)
        case _       : response = protocol.undefined_logic_response
    return JsonResponse(response)

# Handle Category table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_category_crud(request, id):
    match(request.method):
        case    "GET": response = protocol.not_implemented_response
        case   "POST": response = protocol.not_implemented_response
        case    "PUT": response = protocol.not_implemented_response
        case "DELETE": response = protocol.not_implemented_response
        case _       : response = protocol.undefined_logic_response
    return JsonResponse(response)

# Handle User table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_user_crud(request, id=None):
    print("Handle user crud request.data: ", request.data)
    match(request.method):
        case    "GET": response = protocol.not_implemented_response
        case   "POST": response = api_gateway_client.call("auth", "login", request.data, {}, None)
        case    "PUT": response = protocol.not_implemented_response
        case "DELETE": response = protocol.not_implemented_response
        case _       : response = "login response"


    print(response)
    return JsonResponse(response)