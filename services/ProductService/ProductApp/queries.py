from ProductApp.models import Special_Sale, Product, Category, Product_Discount



def event_insert_query():
    b = Special_Sale(name="Halloween")
    b.save()

def event_delete_query():
    b = Special_Sale.objects.get(id="1")
    b.delete()
    
def product_insert_query():
    b = Product(category="shoes", price=20, stock=20, name="vans", description="some nice shoes")
    b.save()

def category_insert_query():
    # Example values for parent_category and name
    
    name = "Example Category"

    # Create an instance of the Category model
    category = Category(name=name)

    # Save the category to the database
    category.save()

def product_discount():
    #special_sale = Special_Sale.objects.get(id="1")
    #product_discount = 
    pass