from ProductApp.models import Special_Sale, Product, Category, Product_Discount


# CRUD event

def event_Insert_Query(event_name):
    b = Special_Sale(name=event_name)
    b.save()

def event_Delete_Query(event_name):

    b = Special_Sale.objects.filter(name=event_name)
    b.delete()

def fetch_All_Events():
    b = Special_Sale.objects.all().values()

def fetch_Specific_Event(event_name):
    b = Special_Sale.objects.filter(name=event_name).values()
    return b


# CRUD category

def category_Insert_Query(name):

    # Create an instance of the Category model
    category = Category(name=name)

    # Save the category to the database
    category.save()

def subcategory_Insert_Query(name,subname):
    category = Category.objects.get(name=name)

    subcategory = Category(name=subname, parent_category=category)

    subcategory.save()

def category_Delete_Query(category_id):
    b = Category.objects.get(id=category_id)
    b.delete()

def fetch_All_Categories():
    b = Category.objects.all().values()

def fetch_Specific_Category(category_name):
    b = Category.objects.filter(name=category_name).values()
    return b

def fetch_Specific_Category_Object(category_name):
    b = Category.objects.get(name=category_name)
    return b

# CRUD product

def create_Product(category_id, product_price, product_stock, product_name, product_description):

    category_instance = Category.objects.get(pk=category_id) 
    
    product = Product(price=product_price, stock=product_stock, name=product_name, description=product_description, category=category_instance)

    product.save()

def product_Delete_Query(product_id):
    b = Product.objects.get(id=product_id)
    b.delete()

def fetch_All_Products():
    b = Product.objects.all().values()


def fetch_Specific_Product(product_name):
    b = Product.objects.filter(name=product_name).values()
    return b

#update products

def update_Product(update_parameter, new_value, product_id):
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

def product_Discount_Insert_Query(discount, special_sale_id, product_id):

    special_sale = Special_Sale.objects.get(pk=special_sale_id)

    product = Product.objects.get(pk=product_id)

    product_discount = Product_Discount(discount=discount, product=product, special_sale=special_sale)

    product_discount.save() 

def product_Discount_Delete_Query(product_id):
    b = Product_Discount.objects.get(id=product_id)
    b.delete()

def fetch_All_Product_Discount():
    b = Product_Discount.objects.all()

def fetch_Specific_Product_Discount(product_name):
    b = Product.objects.get(name=product_name)
    b = Product_Discount.objects.filter(product=b).values()
    return b


def update_Product_Discount(update_parameter, new_value, product_discount_id):
    if(update_parameter=="product"):
        product_instance = Product.objects.get(name=new_value) 
        Product_Discount.objects.filter(pk=product_discount_id).update(product=product_instance)

    elif(update_parameter=="special_sale"):
        special_sale_instance = Special_Sale.objects.get(name=new_value) 
        Product_Discount.objects.filter(pk=product_discount_id).update(special_sale=special_sale_instance)

    elif(update_parameter=="discount"):
        Product_Discount.objects.filter(pk=product_discount_id).update(discount=new_value)

    else:
        return "send a valid update_parameter"
    
