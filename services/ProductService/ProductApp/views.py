from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
#from .APIGatewayServer import ApiGatewayServer
from .queries import *


lookup = {
    "create_event":{
        "func": event_Insert_Query,
        "groups":["admin"],
        "required_fields":[("event_name", str)]
    },
        "create_product":{
        "func": create_Product,
        "groups":["admin"],
        "required_fields":[("category_id", int), ("product_price", int), ("product_stock",int), ("product_name", str), ("product_description",str)]
    },
        "create_product_discount":{
        "func": product_Discount_Insert_Query,
        "groups":["admin"],
        "required_fields":[("discount", int), ("special_sale_id",int), ("product_id",int)]
    },
        "create_category":{
        "func": category_Insert_Query,
        "groups":["admin"],
        "required_fields":[("name", str)]
    },
        "delete_event":{
        "func": event_Delete_Query,
        "groups":["admin"],
        "required_fields":[("event_name", str)]
    },
        "delete_product":{
        "func": product_Delete_Query,
        "groups":["admin"],
        "required_fields":[("product_id", int)]
    },
        "delete_product_discount":{
        "func": product_Discount_Delete_Query,
        "groups":["admin"],
        "required_fields":[("product_id", int)]
    },
        "delete_category":{
        "func": category_Delete_Query,
        "groups":["admin"],
        "required_fields":[("category_id", str)]
    }
}

# Create your views here.
def home(request):
    return HttpResponse("hello world")





