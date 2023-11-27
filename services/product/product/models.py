from django.db import models

# Create your models here.
"""
class Product(models.Model):
    category = models.OneToOneField("category", on_delete=models.PROTECT)
    price = models.IntegerField()
    stock = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Special_Sale(models.Model):
    name = models.CharField(max_length=255)

class Product_Discount(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    special_sale = models.OneToOneField("Special_Sale", on_delete=models.PROTECT)
    discount = models.IntegerField()

class Category(models.Model):
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
"""