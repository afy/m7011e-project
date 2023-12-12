from ProductApp.models import Special_Sale, Product, Category, Product_Discount



def event_insert_query(event_name):
    b = Special_Sale(name=event_name)
    b.save()

def event_delete_query(event_name):

    b = Special_Sale.objects.filter(name=event_name)
    b.delete()
    
def product_insert_query(category, price, stock, name, description):
    b = Product(category=category, price=price, stock=stock, name=name, description=description)
    b.save()

def product_delete_query(product_id):
    b = Product.objects.get(id=product_id)
    b.delete()

def category_insert_query(name):

    # Create an instance of the Category model
    category = Category(name=name)

    # Save the category to the database
    category.save()

def create_product(category_id, product_price, product_stock, product_name, product_description):

    category_instance = Category.objects.get(pk=category_id) 
    
    product = Product(price=product_price, stock=product_stock, name=product_name, description=product_description, category=category_instance)

    product.save()

def product_discount(discount, special_sale_id, product_id):

    special_sale = Special_Sale.objects.get(pk=special_sale_id)

    product = Product.objects.get(pk=product_id)

    product_discount = Product_Discount(discount=discount, product=product, special_sale=special_sale)

    product_discount.save() 

