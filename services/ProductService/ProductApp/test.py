from django.test import TestCase
from ProductApp.models import Product, Product_Discount, Category, Special_Sale

class Special_SaleTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Christmas")
        Product.objects.create(name="Summer")
    
    def test_Special_Sale_Exists(self):
        christmas_event = Special_Sale.objects.get(name="Christmas")
        summer_event = Special_Sale.objects.get(name="Summer")
        self.assertEqual(christmas_event.objects.values_list("name", "Christmas"), "Christmas")
        self.assertEqual(christmas_event.objects.values_list("name", "Summer"), "Summer")