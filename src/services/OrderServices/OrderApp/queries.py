from OrderApp.models import Order, Order_item


# CRUD event

def event_Insert_Order(user_id, payment_status, order_date, total_price, payment_method):
    b = Order(user_id=user_id, payment_status=payment_status, order_date=order_date, total_price=total_price, payment_method=payment_method)
    b.save()