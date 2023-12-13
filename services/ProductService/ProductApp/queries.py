from ProductApp.models import Special_Sale, Product, Category, Product_Discount


# CRUD event

def event_insert_query(event_name):
    b = Special_Sale(name=event_name)
    b.save()

def event_delete_query(event_name):

    b = Special_Sale.objects.filter(name=event_name)
    b.delete()

def fetch_all_events():
    b = Special_Sale.objects.all()

def fetch_specific_event(event_name):
    b = Special_Sale.objects.filter(name=event_name)


# CRUD category

def category_insert_query(name):

    # Create an instance of the Category model
    category = Category(name=name)

    # Save the category to the database
    category.save()

def category_delete_query(category_id):
    b = Category.objects.get(id=category_id)
    b.delete()

def fetch_all_categories():
    b = Category.objects.all()

def fetch_specific_category(category_name):
    b = Category.objects.filter(name=category_name)

# CRUD product

def create_product(category_id, product_price, product_stock, product_name, product_description):

    category_instance = Category.objects.get(pk=category_id) 
    
    product = Product(price=product_price, stock=product_stock, name=product_name, description=product_description, category=category_instance)

    product.save()

def product_delete_query(product_id):
    b = Product.objects.get(id=product_id)
    b.delete()

def fetch_all_products():
    b = Product.objects.all()

def fetch_specific_product(product_name):
    b = Product.objects.filter(name=product_name)

#update products

def update_product(update_parameter, new_value, product_id):
    if(update_parameter=="name"):
        Product.objects.filter(pk=product_id).update(name=new_value)

    elif(update_parameter=="stock"):
        Product.objects.filter(pk=product_id).update(name=new_value)

    elif(update_parameter=="price"):
        Product.objects.filter(pk=product_id).update(name=new_value)

    elif(update_parameter=="description"):
        Product.objects.filter(pk=product_id).update(name=new_value)

    elif(update_parameter=="category"):
        category_instance = Category.objects.get(pk=new_value) 
        Product.objects.filter(pk=product_id).update(category=category_instance)

    else:
        return "send a valid update parameter"

# CRUD product_discount

def product_discount_insert_query(discount, special_sale_id, product_id):

    special_sale = Special_Sale.objects.get(pk=special_sale_id)

    product = Product.objects.get(pk=product_id)

    product_discount = Product_Discount(discount=discount, product=product, special_sale=special_sale)

    product_discount.save() 

def product_discount_delete_query(product_id):
    b = Product_Discount.objects.get(id=product_id)
    b.delete()

def fetch_all_product_discount():
    b = Special_Sale.objects.all()

def fetch_specific_product_discount(product_discount_name):
    b = Special_Sale.objects.filter(name=product_discount_name)

def update_product_discount(update_parameter, new_value, product_discount_id):
    if(update_parameter=="product"):
        product_instance = Product.objects.get(pk=new_value) 
        Product.objects.filter(pk=product_discount_id).update(product=product_instance)

    elif(update_parameter=="special_sale"):
        special_sale_instance = Special_Sale.objects.get(pk=new_value) 
        Product.objects.filter(pk=product_discount_id).update(specia_sale=special_sale_instance)

    elif(update_parameter=="discount"):
        Product.objects.filter(pk=product_discount_id).update(name=new_value)

    else:
        return "send a valid update_parameter"