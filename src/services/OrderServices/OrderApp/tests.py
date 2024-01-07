from django.test import TestCase
from .queries import *
# Create your tests here.
from OrderApp.models import Order, Order_item

class OrderTestCase(TestCase):
    def setUp(self):
        insert_Order(user_id=1, payment_status=1,order_date="28/7",total_price=20,payment_method="Mastercatd" )
        insert_Order(user_id=2, payment_status=0,order_date="26/7",total_price=10,payment_method="Mastercatd")
        insert_Order_Item(1,2,3,5)
        insert_Order_Item(1,2,3,5)
        insert_Order_Item(1,2,3,5)

        insert_Order_Item(2,2,3,5)
        insert_Order_Item(2,2,3,5)
        insert_Order_Item(2,2,3,5)

    
    def test_Orderexists(self):
        order_id_1 = fetch_Specific_Order_With_Items(1)[0]['id']
        order_id_2 = fetch_Specific_Order_With_Items(2)[0]['id']

        self.assertEqual(order_id_1, 1)
        self.assertEqual(order_id_2, 4)
        
    def test_change_payment_status(self):
        update_Payment_status(1,0)
        order_id_1 = fetch_Specific_Order(1)[0]['payment_status']
        self.assertEqual(order_id_1,0)