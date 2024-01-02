from django.db import models
from django.conf import settings


# Create your models here.

class Order(models.Model):
    user_id = models.CharField(max_length=255)
    payment_status = models.IntegerField()
    order_date = models.CharField(max_length=255)
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=255)

    @classmethod
    def create(cls, user_id, payment_status, order_date, total_price, payment_method):
        order = cls(user_id=user_id, paymemt_status=payment_status, order_date=order_date, total_price=total_price, payment_method=payment_method)
        # do something with the book
        return order

    class Meta:
        app_label = 'OrderApp'
