from .queries import *

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from shared.pikacomms.server import PikaServer, PikaServerLookup

def example(body):
    print("Cool!")
    return {}, body.key, "ret", body["reply"]  

lookup_new = PikaServerLookup() 
lookup_new.add("create_product", example, None)
server = PikaServer("prod", lookup_new, "ProdServer")
server.startListening()

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