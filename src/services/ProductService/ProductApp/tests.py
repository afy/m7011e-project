from django.test import TestCase
from .queries import *
# Create your tests here.
from ProductApp.models import Product, Product_Discount, Category, Special_Sale

class Special_SaleTestCase(TestCase):
    def setUp(self):
        event_Insert_Query("Christmas")
        event_Insert_Query("Summer")
    
    def test_Special_Sale_Exists(self):
        christmas_event = fetch_Specific_Event("Christmas")[0]['name']
        summer_event = fetch_Specific_Event("Summer")[0]['name']

        self.assertEqual(christmas_event, "Christmas")
        self.assertEqual(summer_event, "Summer")

class CategoryTestCase(TestCase):
    def setUp(self):
        category_Insert_Query("Shoes")
        category_Insert_Query("Books")

    def test_Categories_Exists(self):
        shoes_categories = fetch_Specific_Category("Shoes")[0]['name']
        books_categories = fetch_Specific_Category("Books")[0]['name']      

        self.assertEqual(shoes_categories, "Shoes")
        self.assertEqual(books_categories, "Books")

    def test_Subcategories_Exists(self):
        shoes_categories = fetch_Specific_Category_Object("Shoes")
        books_categories = fetch_Specific_Category_Object("Books")

        subcategory_Insert_Query("Shoes", "Clothes")
        subcategory_Insert_Query("Books", "Pockets")

        clothes_categories = fetch_Specific_Category("Clothes")[0]['name']
        pockets_categories = fetch_Specific_Category("Pockets")[0]['name']  

        self.assertEqual(clothes_categories, "Clothes")
        self.assertEqual(pockets_categories, "Pockets")
        

class ProductTestCase(TestCase):
    def setUp(self):
        category_Insert_Query("Shoes")
        category_Insert_Query("Books")
        create_Product(category_id=1,product_price=30,product_stock=30,product_name="shoes",product_description="nice shoes")
        create_Product(category_id=1,product_price=40,product_stock=40,product_name="vans",product_description="nice vans")

    def test_Products_exists(self):
        print()
        shoes_products = fetch_Specific_Product("shoes")[0]['name']
        vans_products = fetch_Specific_Product("vans")[0]['name']

        self.assertEqual(shoes_products, "shoes")
        self.assertEqual(vans_products, "vans")

class Product_discountTestCase(TestCase):
    def setUp(self):
        event_Insert_Query("Christmas")
        event_Insert_Query("Summer")
        category_Insert_Query("Shoes")
        category_Insert_Query("Books")
        create_Product(category_id=1,product_price=30,product_stock=30,product_name="shoes",product_description="nice shoes")
        create_Product(category_id=1,product_price=40,product_stock=40,product_name="vans",product_description="nice vans")
        product_Discount_Insert_Query(discount=20,special_sale_id=1,product_id=1)
        product_Discount_Insert_Query(discount=40,special_sale_id=1,product_id=2)

    def test_Product_discount_exists(self):
        
        shoes_discount = fetch_Specific_Product_Discount("shoes")[0]['discount']
        vans_discount = fetch_Specific_Product_Discount("vans")[0]['discount']

        self.assertEqual(shoes_discount, 20)
        self.assertEqual(vans_discount, 40)

    def test_update_product_discount_product_name(self):
        update_Product_Discount("product","vans",1)
        update_Product_Discount("product","shoes",2)

        shoes_discount = fetch_Specific_Product_Discount("shoes")[0]['discount']
        vans_discount = fetch_Specific_Product_Discount("vans")[0]['discount']

        self.assertEqual(shoes_discount, 40)
        self.assertEqual(vans_discount, 20)

    def test_update_product_discount_special_sale(self):
        update_Product_Discount("special_sale","Summer",1)
        update_Product_Discount("special_sale","Summer",2)

        shoes_discount = fetch_Specific_Product_Discount("shoes")[0]['special_sale_id']
        vans_discount = fetch_Specific_Product_Discount("vans")[0]['special_sale_id']

        self.assertEqual(shoes_discount, 2)
        self.assertEqual(vans_discount, 2)
    
    def test_update_product_discount(self):
        update_Product_Discount("discount",60,1)
        update_Product_Discount("discount",60,2)

        shoes_discount = fetch_Specific_Product_Discount("shoes")[0]['discount']
        vans_discount = fetch_Specific_Product_Discount("vans")[0]['discount']

        self.assertEqual(shoes_discount, 60)
        self.assertEqual(vans_discount, 60)






