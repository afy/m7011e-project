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

lookup.add("fetch-all-products", fetch_All_Products, ["user"], [()])

lookup.add("fetch-specific-product", fetch_Specific_Product, ["user"], [("product_name",str)])

lookup.add("update_Product", update_Product, ["admin"], [("update_parameter",str), ("new_value",str),("product_id",int)])

# Category

lookup.add("category_Insert_Query", category_Insert_Query, ["admin"], [("name",str)])

lookup.add("subcategory_Insert_Query", subcategory_Insert_Query, ["admin"], [("name",str), ("subname",str)])

lookup.add("category_Delete_Query", category_Delete_Query, ["admin"], [("category_id",int)])

lookup.add("fetch_All_Categories", fetch_All_Categories, ["user"], [()]) #ska dem vara tomma om dem inte tar några argument?

lookup.add("fetch_Specific_Category", fetch_Specific_Category, ["user"], [("category_name",int)])

lookup.add("fetch_Specific_Category_Object", fetch_Specific_Category_Object, ["admin"], [("category_name",str)])

lookup.add("update_Category", update_Category, ["admin"], [("name",str),("newname",str)])

# Special_sale

lookup.add("event_Insert_Query", event_Insert_Query, ["admin"], [("event_name",str)])

lookup.add("event_Delete_Query", event_Delete_Query, ["admin"], [("event_name",str)])

lookup.add("fetch_All_Events", fetch_All_Events, ["user"], [()])

lookup.add("fetch_Specific_Event", fetch_Specific_Event, ["admin"], [("event_name",str)])

lookup.add("update_Event", update_Event, ["admin"], [("name",str),("newname",str)])

# Product_discount

lookup.add("product_Discount_Insert_Query", product_Discount_Insert_Query, ["admin"], [("discount",int),("special_sale_id", int),("product_id",int)])

lookup.add("product_Discount_Delete_Query", product_Discount_Delete_Query, ["admin"], [("product_id",int)])

lookup.add("fetch_Specific_Product_Discount", fetch_Specific_Product_Discount, ["user"], [("product_name",str)])

lookup.add("update_Product_Discount", update_Product_Discount, ["admin"], [("update_parameter",int),("new_value", int),("product_discount_id",int)])


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