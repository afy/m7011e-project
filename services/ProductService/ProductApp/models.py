from django.db import models
from django.conf import settings


# Create your models here.

class Product(models.Model):
    category = models.OneToOneField("category", on_delete=models.PROTECT)
    price = models.IntegerField()
    stock = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

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
    special_sale = models.OneToOneField("Special_Sale", on_delete=models.PROTECT)
    discount = models.IntegerField()
    class Meta:
        app_label = 'ProductApp'

class Category(models.Model):
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    class Meta:
        app_label = 'ProductApp'

