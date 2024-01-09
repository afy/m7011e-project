from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .APIGatewayServer import ApiGatewayServer
from .queries import *
import time
from django.http import HttpResponse
from django.template import loader


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from shared.pikacomms.server import PikaServer, PikaServerLookup

def example(body):
    print("Func-call")
    return {"test-response-data": "example-data", "body-sent": body}

def example_timeout(body):
    print("Initializing timeout for 15 seconds")
    time.sleep(15)
    return {"timeout": "15s"}

# Init lookup
lookup = PikaServerLookup() 
lookup.add("test-function", example, None, None)
lookup.add("test-timeout", example_timeout, None, None)

#order CRUD

lookup.add("insert_Order", insert_Order, ["user"], [("user_id",int),("payment_status",int),("order_date",str),("total_price",int),("payment_method")])

lookup.add("fetch_Specific_Order", fetch_Specific_Order, ["user"],  [("order_id",int)])

lookup.add("fetch_All_Orders", fetch_All_Orders, ["user"],  [()])

lookup.add("delete_Order", delete_Order, ["user"],  [("order_id",int)])

lookup.add("update_Payment_Status", update_Payment_Status, ["user"],  [("order_id",int),("payment_status",int)])

lookup.add("fetch_All_Orders", fetch_All_Orders, ["user"],  [()])

#order_item CRUD

lookup.add("insert_Order_Item", insert_Order_Item, ["user"],  [("order_id",int),("price",int),("count",int),("product_id",int)])

lookup.add("fetch_Specific_Order_With_Items", fetch_Specific_Order_With_Items, ["user"],  [("order_id",int)])

lookup.add("delete_Order_Item", delete_Order_Item, ["user"],  [("order_id",int)])

lookup.add("update_Price_Order_Item", update_Price_Order_Item, ["user"],  [("order_item_id",int)])

# Create your views here.


def home(request):
  
  orders = fetch_All_Orders()
  order_items= fetch_All_Order_Items()
  template = loader.get_template('myfirst.html')
  return render(request, 'myfirst.html', {'orders': orders, 'order_items':order_items})

