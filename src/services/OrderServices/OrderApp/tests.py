from django.test import TestCase
from .queries import *
# Create your tests here.
from OrderApp.models import Order, Order_item

class OrderTestCase(TestCase):
    def setUp(self):
        event_Insert_Order("Christmas")
        event_Insert_Order("Summer")
    
   # def test_Orderexists(self):
        #christmas_event = fetch_Specific_Event("Christmas")[0]['name']
        #summer_event = fetch_Specific_Event("Summer")[0]['name']

      #  self.assertEqual(christmas_event, "Christmas")
      #  self.assertEqual(summer_event, "Summer")