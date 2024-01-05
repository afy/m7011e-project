from .queries import *
import time

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

# Product
lookup.add(
    "create-product", create_Product, ["admin"], 
    [("category_id", int), ("product_price", int), ("product_stock",int), ("product_name", str), ("product_description",str)])

lookup.add("delete-product", product_Delete_Query, ["admin"],
    [("product_id", int)])

# Category
# Special_sale
# Product_discount

server = PikaServer("prod", lookup, "Product Server")
server.startListening()




lookup_old = {
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