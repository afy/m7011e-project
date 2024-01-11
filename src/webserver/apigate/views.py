from django.http import JsonResponse
from rest_framework.decorators import api_view

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared.pikacomms.client import PikaClient
from shared.pikacomms import protocol

# Tables: Product, Special_Sale, Product_Discount, Category, User

# Communicate with microservices
api_gateway_client = PikaClient(name="API Gateway", log_params=True, timeout=5)


def validateCall(req):
    if "token" in req.data and req.data["token"]:
        resp = api_gateway_client.call("auth", "token-auth", {"token": req.data["token"]}, None)

        return {"id": None, "groups": resp["groups"]} if "groups" in resp else {"id": None, "groups": ['']}
    else:
        return {"id": None, "groups": ['']}

# Handle Product table CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_product_crud(request):
    match(request.method):
        case    "GET": response = api_gateway_client.call("prod", "get-product",
                                                           request.data, validateCall(request))
        case   "POST": response = api_gateway_client.call("prod", "get-product", 
                                                           request.data, validateCall(request))
        case    "PUT": response = api_gateway_client.call("prod", "create-product",
                                                           request.data, validateCall(request))
        case "DELETE": response = api_gateway_client.call("prod", "delete-product", 
                                                           request.data, validateCall(request))
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
        case   "POST": response = api_gateway_client.call("auth", "login", request.data, validateCall(request), None)
        case    "PUT": response = protocol.not_implemented_response
        case "DELETE": response = protocol.not_implemented_response
        case _       : response = protocol.undefined_logic_response


    print(response)
    return JsonResponse(response)

@api_view(["POST"])
def verify_token(request):
    resp = api_gateway_client.call("auth", "token-auth", request.data, validateCall(request), None)
    return JsonResponse(resp)