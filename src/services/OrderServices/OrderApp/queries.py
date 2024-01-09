from OrderApp.models import Order, Order_item


# CRUD event

#insert the customers order into the database

def insert_Order(user_id, payment_status, order_date, total_price, payment_method):
    b = Order(user_id=user_id, payment_status=payment_status, order_date=order_date, total_price=total_price, payment_method=payment_method)
    b.save()

#insert the customers order item into the database

def insert_Order_Item(order_id, price, count, product_id):

    order_instance = Order.objects.get(pk=order_id) 
    
    product = Order_item(order_id=order_instance, price=price, count=count, product_id=product_id)

    product.save()

# fetch the customers order from the database with items

def fetch_Specific_Order_With_Items(order_id):
    order_instance = Order.objects.get(pk=order_id)

    order_item_instance = Order_item.objects.filter(order_id=order_instance).values()

    return order_item_instance

# fetch the customers order from the database without items

def fetch_Specific_Order(order_id):
    order_instance = Order.objects.filter(pk=order_id).values()

    return order_instance

#fetch all orders

def fetch_All_Orders_For_User(user_id):
    order_instance = Order.objects.filter(user_id=user_id).values()

    print(order_instance)
    
    return order_instance


#fetch all orders

def fetch_All_Orders():
    order_instance = Order.objects.all().values()

    print(order_instance)
    
    return order_instance

def fetch_All_Order_Items():
    order_instance = Order_item.objects.all().values()

    print(order_instance)
    
    return order_instance

#udate price in order_item

def delete_Order(order_id):
    b = Order.objects.get(id=order_id)
    b.delete()


def delete_Order_Item(order_item_id):
    b = Order_item.objects.get(id=order_item_id)
    b.delete()

def update_Price_Order_Item(order_item_id, price):
    Order_item.objects.filter(pk=order_item_id).update(price=price)

#update payment status

def update_Payment_Status(order_id, payment_status):
    Order.objects.filter(pk=order_id).update(payment_status=payment_status)
    
    b = Order.objects.filter(pk=order_id).values()
    