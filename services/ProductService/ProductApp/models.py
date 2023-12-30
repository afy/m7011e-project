from django.db import models
from django.conf import settings


# Create your models here.

class Product(models.Model):
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    price = models.IntegerField()
    stock = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    @classmethod
    def create(cls, price, stock, name, description, category_instance):
        product = cls(price=price, stock=stock, name=name, description=description, category=category_instance)
        # do something with the book
        return product

    class Meta:
        app_label = 'ProductApp'

class Special_Sale(models.Model):
    name = models.CharField(max_length=255)

    @classmethod
    def create(cls, name):
        name = cls(name=name)
        # do something with the book
        return name
    class Meta:
        app_label = 'ProductApp'

class Product_Discount(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    special_sale = models.ForeignKey("Special_Sale", on_delete=models.PROTECT)
    discount = models.IntegerField()
    @classmethod
    def create(cls, discount, product, special_sale):
        product_discount = cls(discount=discount, product=product, special_sale=special_sale)
        # do something with the book
        return product_discount
    class Meta:
        app_label = 'ProductApp'

class Category(models.Model):
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=255)

    @classmethod
    def create(cls, name):
        name = cls(name=name)
        return name
    
    class Meta:
        app_label = 'ProductApp'

